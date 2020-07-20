"""Admin module for users app."""
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet

from .models import Request, Sponsor
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class RequestResource(resources.ModelResource):
    """ModelResource is Resource subclass for handling Django models."""

    class Meta:
        """Meta data."""

        model = Request
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "country",
            "city",
            "date_of_birth",
            "blood_type",
            "message",
            "height",
            "weight",
            "blood_pressure",
            "allergies",
            "medical_conditions",
            "organ_date_registration",
            "is_accepted",
            "created_at",
            "organs_to_be_donated",
        )


class SponsorResource(resources.ModelResource):
    """ModelResource is Resource subclass for handling Django models."""

    class Meta:
        """Meta data."""

        model = Sponsor
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "country",
            "city",
            "amount",
            "created_at",
        )


@admin.register(Request)
class RequestAdmin(ImportExportActionModelAdmin):
    """Configure the request model in admin page."""

    resource_class = RequestResource

    date_hierarchy = "created_at"

    list_display = (
        "first_name",
        "last_name",
        "blood_type",
        "is_accepted",
        "created_at",
    )

    ordering = (
        "first_name",
        "last_name",
        "blood_type",
        "is_accepted",
        "created_at",
    )

    list_filter = ("is_accepted",)

    search_fields = ("first_name", "last_name")

    actions = ["export_admin_action", "accept_donation", "deny_donation"]

    def accept_donation(
        self: "RequestAdmin", request: WSGIRequest, queryset: QuerySet
    ) -> None:
        """Custom action that update the status to request."""
        queryset.update(is_accepted=True)

    def deny_donation(
        self: "RequestAdmin", request: WSGIRequest, queryset: QuerySet
    ) -> None:
        """Custom action that update the status to not request."""
        queryset.update(is_accepted=False)

    accept_donation.short_description = "Mark selected Request as Accepted"
    deny_donation.short_description = "Mark selected Request as not Deny"


@admin.register(Sponsor)
class SponsorAdmin(ImportExportActionModelAdmin):
    """Configure the sponsor model in admin page."""

    resource_class = SponsorResource

    date_hierarchy = "created_at"

    list_display = (
        "first_name",
        "last_name",
        "country",
        "amount",
        "created_at",
    )

    ordering = (
        "first_name",
        "last_name",
        "country",
        "amount",
        "created_at",
    )

    list_filter = ("amount", "created_at")

    search_fields = ("first_name", "last_name", "amount")
