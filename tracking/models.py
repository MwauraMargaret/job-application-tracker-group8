from django.db import models

from django.contrib.auth.models import AbstractUser

#user
class User(AbstractUser):
    ROLE_CHOICES = [
        ('applicant', 'Applicant'),
        ('recruiter', 'Recruiter'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='applicant')


# Company
class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Job
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} @ {self.company.name}"


# Application
class Application(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("screening", "Screening"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    resume_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="applied")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"


# Interview
class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="interviews")
    scheduled_for = models.DateTimeField()
    mode = models.CharField(max_length=50, blank=True)  # e.g., Onsite/Zoom
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Interview for {self.application.applicant.username} on {self.scheduled_for}"# Create your models here.
