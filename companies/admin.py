"""Django admin configuration for the companies app."""

from django.contrib import admin

from .models import Company, CompanyMember


class CompanyMemberInline(admin.TabularInline):
    model = CompanyMember
    extra = 0
    autocomplete_fields = ["user"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "industry",
        "size",
        "location",
        "is_verified",
        "created_at",
    ]

    list_filter = [
        "size",
        "industry",
        "is_verified",
    ]

    search_fields = [
        "name",
        "slug",
        "location",
    ]

    prepopulated_fields = {"slug": ("name",)}

    inlines = [CompanyMemberInline]


@admin.register(CompanyMember)
class CompanyMemberAdmin(admin.ModelAdmin):
    list_display = [
        "company",
        "user",
        "role",
        "created_at",
    ]

    list_filter = [
        "role",
    ]

    search_fields = [
        "company__name",
        "user__email",
    ]

    autocomplete_fields = ["company", "user"]
