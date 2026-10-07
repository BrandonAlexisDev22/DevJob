"""Django admin configuration for the applications app."""

from django.contrib import admin

from .models import Application, ApplicationStatusHistory


class ApplicationStatusHistoryInline(admin.TabularInline):
    model = ApplicationStatusHistory
    extra = 0
    readonly_fields = ["changed_at"]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "applicant",
        "job_offer",
        "status",
        "created_at",
    ]

    list_filter = [
        "status",
    ]

    search_fields = [
        "applicant__email",
        "job_offer__title",
    ]

    autocomplete_fields = ["job_offer", "applicant"]
    inlines = [ApplicationStatusHistoryInline]
