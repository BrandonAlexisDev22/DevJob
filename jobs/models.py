"""Data models for the jobs app."""

import uuid

from django.db import models
from django.utils.text import slugify

from companies.models import Company
from core.models import TimeStampedModel


class Technology(models.Model):
    """A technology/skill a job offer requires, e.g. Python, React."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "technologies"

    def save(self, *args, **kwargs):
        """Auto-generate the slug from the name on first save."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class JobOffer(TimeStampedModel):
    """A job offer published by a company."""

    class Modality(models.TextChoices):
        REMOTE = "REMOTE", "Remote"
        HYBRID = "HYBRID", "Hybrid"
        ONSITE = "ONSITE", "On-site"

    class ContractType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full time"
        PART_TIME = "PART_TIME", "Part time"
        FREELANCE = "FREELANCE", "Freelance"
        INTERNSHIP = "INTERNSHIP", "Internship"

    class Seniority(models.TextChoices):
        JUNIOR = "JUNIOR", "Junior"
        MID = "MID", "Mid level"
        SENIOR = "SENIOR", "Senior"
        LEAD = "LEAD", "Lead"

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        CLOSED = "CLOSED", "Closed"

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_offers"
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    technologies = models.ManyToManyField(
        Technology, related_name="job_offers", blank=True
    )
    modality = models.CharField(max_length=20, choices=Modality.choices)
    contract_type = models.CharField(max_length=20, choices=ContractType.choices)
    seniority = models.CharField(max_length=20, choices=Seniority.choices)
    location = models.CharField(max_length=150, blank=True)
    salary_min = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    salary_max = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    currency = models.CharField(max_length=3, default="USD")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        """Auto-generate a unique slug from the title on first save."""
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} @ {self.company.name}"
