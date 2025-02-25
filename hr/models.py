from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Department name (unique)")
    description = models.TextField(blank=True, null=True, help_text="Optional department description")

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50, help_text="Employee's first name")
    last_name = models.CharField(max_length=50, help_text="Employee's last name")
    email = models.EmailField(unique=True, help_text="Employee email (must be unique)")
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name='employees',
        help_text="Department the employee belongs to"
    )
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"