from django.db import models
from hr.models import Employee

class Evaluation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.CharField(max_length=100, help_text="Name of the evaluator")
    score = models.IntegerField(help_text="Evaluation score (e.g., 1-10)")
    comments = models.TextField(blank=True, help_text="Additional comments")
    evaluated_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation for {self.employee} on {self.evaluated_on}"