from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.membership.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")
