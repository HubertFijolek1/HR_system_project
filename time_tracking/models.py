from django.db import models
from hr.models import Employee

class TimeEntry(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='time_entries')
    clock_in = models.DateTimeField(help_text="Time when the employee clocked in")
    clock_out = models.DateTimeField(help_text="Time when the employee clocked out", null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.clock_in.strftime('%Y-%m-%d %H:%M')}"