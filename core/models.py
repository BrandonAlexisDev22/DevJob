"""Shared abstract base models used across the project's apps."""

from django.db import models


class TimeStampedModel(models.Model):
    """Adds creation/update timestamps to a model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
