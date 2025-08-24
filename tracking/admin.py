from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Company, Job, Application, Interview

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("role",)}),  # include role in admin
    )
    list_display = ("username", "email", "role", "is_staff", "is_superuser")

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "website", "owner", "created_at")

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "company", "location", "salary_min", "salary_max", "deadline", "created_at")

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "job", "applicant", "status", "submitted_at")

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("id", "application", "scheduled_for", "mode")
