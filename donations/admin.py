"""Admin module for users app."""
from django.contrib import admin

from .models import Blood, Sponsor, Organ, Acceptor


@admin.register(Blood)
class BloodAdmin(admin.ModelAdmin):
    """Configure the request model in admin page."""

    date_hierarchy = "created_at"

    list_display = (
        "donor",
        "blood_type",
    )

    ordering = (
        "donor",
        "blood_type",
    )

    list_filter = ("last_donate_date",)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    """Configure the sponsor model in admin page."""

    date_hierarchy = "created_at"

    list_display = (
        "donor",
        "organization",
        "amount",
        "created_at",
    )

    ordering = (
        "donor",
        "organization",
        "amount",
        "created_at",
    )

    list_filter = ("amount", "created_at", "organization")


@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    """Configure the organ model in admin page."""

    date_hierarchy = "created_at"

    list_display = (
        "donor",
        "organ",
        "organ_date_registration",
        "created_at",
    )

    ordering = (
        "donor",
        "organ",
        "organ_date_registration",
        "created_at",
    )

    list_filter = ("organ", "created_at")


@admin.register(Acceptor)
class AcceptorAdmin(admin.ModelAdmin):
    """Configure the acceptor model in admin page."""

    date_hierarchy = "created_at"

    list_display = (
        "name",
        "picture",
        "created_at",
    )

    ordering = (
        "name",
        "picture",
        "created_at",
    )

    list_filter = ("created_at",)

