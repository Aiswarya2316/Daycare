from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Staf(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AdminReg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Child(models.Model):
    staff = models.ForeignKey(Staf, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    admission_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="child_images/", blank=True, null=True)
    medical_health = models.TextField(blank=True, null=True)  # New Field for Health Records
    fee_status = models.CharField(
        max_length=20,
        choices=[("Paid", "Paid"), ("Pending", "Pending"), ("Overdue", "Overdue")],
        default="Pending"
    )  # New Field for Fee Status

    def __str__(self):
        return self.name


class FeeTransaction(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="fees")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("Paid", "Paid"), ("Pending", "Pending"), ("Overdue", "Overdue")],
        default="Pending"
    )

    def __str__(self):
        return f"Fee for {self.child.name} - {self.status}"


class DailyActivity(models.Model):
    staff = models.ForeignKey(Staf, on_delete=models.CASCADE, related_name="activities")
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="daily_activities")
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Activity for {self.child.name} on {self.date}"