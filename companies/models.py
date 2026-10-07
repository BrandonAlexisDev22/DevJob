"""Data models for the companies app."""

from django.db import models
from django.utils.text import slugify

from core.models import TimeStampedModel
from users.models import User


class Company(TimeStampedModel):
    """A company that publishes job offers on the platform."""

    class Size(models.TextChoices):
        STARTUP = "STARTUP", "1-10 employees"
        SMALL = "SMALL", "11-50 employees"
        MEDIUM = "MEDIUM", "51-200 employees"
        LARGE = "LARGE", "201-1000 employees"
        ENTERPRISE = "ENTERPRISE", "1000+ employees"

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)
    location = models.CharField(max_length=150, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=20, choices=Size.choices, blank=True)
    is_verified = models.BooleanField(default=False)

    members = models.ManyToManyField(
        User,
        through="CompanyMember",
        related_name="companies",
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "companies"

    def save(self, *args, **kwargs):
        """Auto-generate the slug from the name on first save."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CompanyMember(TimeStampedModel):
    """A user who belongs to a company, e.g. its owner or a recruiter."""

    class MemberRole(models.TextChoices):
        OWNER = "OWNER", "Owner"
        RECRUITER = "RECRUITER", "Recruiter"

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="memberships"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="company_memberships"
    )
    role = models.CharField(
        max_length=20, choices=MemberRole.choices, default=MemberRole.RECRUITER
    )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("company", "user")

    def __str__(self):
        return f"{self.user.email} @ {self.company.name}"
