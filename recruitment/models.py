from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=50, help_text="Candidate's first name")
    last_name = models.CharField(max_length=50, help_text="Candidate's last name")
    email = models.EmailField(unique=True, help_text="Candidate email")
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    applied_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"