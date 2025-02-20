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
    image = models.ImageField(upload_to="child_images/", blank=True, null=True)  # Image Upload Field

    def __str__(self):
        return self.name


class DailyActivity(models.Model):
    staff = models.ForeignKey(Staf, on_delete=models.CASCADE, related_name="activities")
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="daily_activities")
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Activity for {self.child.name} on {self.date}"