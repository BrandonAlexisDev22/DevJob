"""Django admin configuration for the jobs app."""

from django.contrib import admin

from .models import JobOffer, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "company",
        "modality",
        "contract_type",
        "seniority",
        "status",
        "salary_min",
        "salary_max",
        "published_at",
    ]

    list_filter = [
        "status",
        "modality",
        "contract_type",
        "seniority",
    ]

    search_fields = [
        "title",
        "company__name",
    ]

    autocomplete_fields = ["company"]
    filter_horizontal = ["technologies"]
    readonly_fields = ["slug"]
    date_hierarchy = "published_at"
