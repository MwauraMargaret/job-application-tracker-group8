from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import User, Company

@receiver(post_save, sender=User)
def create_role_defaults(sender, instance, created, **kwargs):
    """
    When a user is created, enforce role-specific defaults.
    """
    if created:
        if instance.role == "applicant":
            # Applicants don't own companies; nothing extra to create yet
            print(f"Applicant account created: {instance.username}")
        elif instance.role == "recruiter":
            # For recruiters, we could auto-assign them an empty Company placeholder (optional)
            print(f"Recruiter account created: {instance.username}")

@receiver(post_save, sender=User)
def create_recruiter_company(sender, instance, created, **kwargs):
    if created and instance.role == "recruiter":
        Company.objects.create(
            name=f"{instance.username}'s Company",
            owner=instance
        )