"""Data models for the applications app."""

from django.db import models

from core.models import TimeStampedModel
from jobs.models import JobOffer
from users.models import User


class Application(TimeStampedModel):
    """A developer's application to a job offer."""

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_REVIEW = "IN_REVIEW", "In review"
        INTERVIEW = "INTERVIEW", "Interview"
        REJECTED = "REJECTED", "Rejected"
        ACCEPTED = "ACCEPTED", "Accepted"

    job_offer = models.ForeignKey(
        JobOffer, on_delete=models.CASCADE, related_name="applications"
    )
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    cover_letter = models.TextField(blank=True)
    resume_url = models.URLField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("job_offer", "applicant")

    def __str__(self):
        return f"{self.applicant.email} -> {self.job_offer.title}"


class ApplicationStatusHistory(models.Model):
    """Audit trail of status changes for an application."""

    application = models.ForeignKey(
        Application, on_delete=models.CASCADE, related_name="status_history"
    )
    status = models.CharField(max_length=20, choices=Application.Status.choices)
    changed_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ["-changed_at"]
        verbose_name_plural = "application status histories"

    def __str__(self):
        return f"{self.application} -> {self.status}"
