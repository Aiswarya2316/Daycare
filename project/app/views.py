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