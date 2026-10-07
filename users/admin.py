"""Django admin configuration for the users app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "phone",
        "role",
        "is_active",
        "is_staff",
    ]

    list_filter = [
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
    ]

    search_fields = [
        "email",
        "first_name",
        "last_name",
        "phone",
        "username",
    ]

    ordering = [
        "-create_at",
    ]

    readonly_fields = [
        "last_login",
        "date_joined",
        "create_at",
        "update_at",
    ]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "phone", "role")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined", "create_at", "update_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "phone",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    filter_horizontal = ("groups", "user_permissions")
