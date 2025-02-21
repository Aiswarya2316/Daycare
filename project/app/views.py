from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



def parenthome(request):
    return render(request,'parent/parenthome.html')



# Customer Registration
def customer_register(request):
    if request.method == "POST":
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer registered successfully!")
            return redirect("login")
    else:
        form = ParentRegistrationForm()
    return render(request, "parent/register.html", {"form": form, "user_type": "Customer"})



# Seller Registration
def seller_register(request):
    if request.method == "POST":
        form = StafRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Seller registered successfully!")
            return redirect("login")
    else:
        form = StafRegistrationForm()
    return render(request, "staf/register.html", {"form": form, "user_type": "Seller"})



# Admin Registration
def admin_register(request):
    if request.method == "POST":
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin registered successfully!")
            return redirect("login")
    else:
        form = AdminRegistrationForm()
    return render(request, "admin/register.html", {"form": form, "user_type": "Admin"})



# Login View
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # Check in all user models
            user = None
            redirect_url = "login"  # Default in case of failure
            if Parent.objects.filter(email=email, password=password).exists():
                user = Parent.objects.get(email=email)
                request.session["user_type"] = "Customer"
                redirect_url = "parenthome"
            elif Staf.objects.filter(email=email, password=password).exists():
                user = Staf.objects.get(email=email)
                request.session["user_type"] = "Seller"
                redirect_url = "stafhome"
            elif AdminReg.objects.filter(email=email, password=password).exists():
                user = AdminReg.objects.get(email=email)
                request.session["user_type"] = "Admin"
                redirect_url = "adminhome"
            if user:
                request.session["user_id"] = user.id
                messages.success(request, f"Welcome {user.name}!")
                return redirect(redirect_url)  # Redirect based on user type
            else:
                messages.error(request, "Invalid credentials")
    form = LoginForm()
    return render(request, "login.html", {"form": form})



# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")


def home(request):
    return render(request,'home.html')



def stafhome(request):
    return render(request,'staf/stafhome.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Child, Staf
from .forms import ChildForm

def add_child(request):
    # Check if user is logged in as staff
    if "user_id" not in request.session or request.session["user_type"] != "Seller":
        messages.error(request, "You must be logged in as staff to add a child.")
        return redirect("login")

    # Fetch the logged-in staff instance
    staff = Staf.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        form = ChildForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.staff = staff  # Assign the staff instance
            child.save()
            messages.success(request, "Child added successfully!")
            return redirect("view_children")
    else:
        form = ChildForm()
    
    return render(request, "staf/add_child.html", {"form": form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Child, Staf, FeeTransaction
from .forms import ChildForm, FeeTransactionForm

def edit_child_details(request, child_id):
    if "user_id" not in request.session or request.session["user_type"] != "Seller":
        messages.error(request, "You must be logged in as staff to edit child details.")
        return redirect("login")

    child = get_object_or_404(Child, id=child_id)

    if request.method == "POST":
        form = ChildForm(request.POST, request.FILES, instance=child)
        if form.is_valid():
            form.save()
            messages.success(request, "Child details updated successfully!")
            return redirect("view_children")
    else:
        form = ChildForm(instance=child)

    return render(request, "staf/edit_child.html", {"form": form, "child": child})



def add_fee_transaction(request):
    if "user_id" not in request.session or request.session["user_type"] != "Seller":
        messages.error(request, "You must be logged in as staff to add fee transactions.")
        return redirect("login")

    if request.method == "POST":
        form = FeeTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fee transaction added successfully!")
            return redirect("view_fees")
    else:
        form = FeeTransactionForm()

    return render(request, "staf/add_fee.html", {"form": form})



def view_fees(request):
    if "user_id" not in request.session or request.session["user_type"] != "Seller":
        messages.error(request, "You must be logged in as staff to view fee details.")
        return redirect("login")

    fees = FeeTransaction.objects.all().order_by("-date_paid")

    return render(request, "staf/view_fees.html", {"fees": fees})




def view_children(request):
    if "user_id" not in request.session or request.session["user_type"] != "Seller":
        messages.error(request, "You must be logged in as staff to view children.")
        return redirect("login")

    children = Child.objects.all().order_by("name")  # Order by name alphabetically

    return render(request, "staf/view_children.html", {"children": children})




from django.shortcuts import render, redirect
from .models import DailyActivity, Child
from .forms import DailyActivityForm

# ✅ Add Daily Activity
def add_daily_activity(request):
    if request.method == "POST":
        form = DailyActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.staff = Staf.objects.first()  # Temporary Fix (Use proper authentication later)
            activity.save()
            return redirect('list_daily_activity')  # Redirect to list view after saving
    else:
        form = DailyActivityForm()
    
    return render(request, 'staf/add_daily_activity.html', {'form': form})


# ✅ View Daily Activities
def list_daily_activity(request):
    activities = DailyActivity.objects.all().order_by('-date')  # Show latest first
    return render(request, 'staf/list_daily_activity.html', {'activities': activities})

















from django.shortcuts import render
from .models import Child, FeeTransaction

def child_list(request):
    """Displays all children with a search option."""
    query = request.GET.get("search")
    if query:
        children = Child.objects.filter(name__icontains=query)
    else:
        children = Child.objects.all().order_by("name")   
    return render(request, "parent/child_list.html", {"children": children})




def child_fee_details(request, child_id):
    """Displays fee details for a specific child."""
    child = Child.objects.get(id=child_id)
    fee_transactions = FeeTransaction.objects.filter(child=child)
    
    return render(request, "parent/child_fee_details.html", {"child": child, "fee_transactions": fee_transactions})




import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Child, FeeTransaction

def process_payment(request, child_id):
    child = get_object_or_404(Child, id=child_id)

    # Get the pending or overdue fee transaction
    fee_transaction = FeeTransaction.objects.filter(child=child, status__in=["Pending", "Overdue"]).order_by('-date_paid').first()

    if not fee_transaction:
        return render(request, "parent/payment_error.html", {"message": "No pending fees found."})

    # Razorpay Client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create Order
    order_data = {
        "amount": int(fee_transaction.amount * 100),  # Convert amount to paise (₹1 = 100 paise)
        "currency": "INR",
        "payment_capture": 1,  # Auto capture payment
    }
    order = client.order.create(data=order_data)

    # Save Order ID to pass it to frontend
    request.session["razorpay_order_id"] = order["id"]

    return render(request, "parent/payment.html", {
        "child": child,
        "fee_transaction": fee_transaction,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "order_id": order["id"],
        "amount": fee_transaction.amount,
    })




def payment_success(request, child_id):
    child = get_object_or_404(Child, id=child_id)

    # Update the latest pending fee transaction
    fee_transaction = FeeTransaction.objects.filter(child=child, status__in=["Pending", "Overdue"]).order_by('-date_paid').first()

    if fee_transaction:
        fee_transaction.status = "Paid"
        fee_transaction.save()

    # Update child's overall fee status if all transactions are paid
    if not FeeTransaction.objects.filter(child=child, status__in=["Pending", "Overdue"]).exists():
        child.fee_status = "Paid"
        child.save()

    return render(request, "parent/payment_success.html", {"child": child})
