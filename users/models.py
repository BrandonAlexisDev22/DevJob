"""Data models for the users app."""

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user for DevJob, identified by email.

    Every account is either a developer looking for jobs or a company
    publishing job offers, as defined by ``role``.
    """

    class Role(models.TextChoices):
        """Account types available on the platform."""

        DEVELOPER = "DEVELOPER", "Developer"
        COMPANY = "COMPANY", "Company"
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    # Optional, but must be unique when provided.
    phone = models.CharField(unique=True, null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.DEVELOPER
    )
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the user's email as its readable representation."""
        return self.email
