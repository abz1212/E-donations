from django.contrib import admin

from .models import Contact
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class ContactResource(resources.ModelResource):
    """ModelResource is Resource subclass for handling Django models."""

    class Meta:
        """Meta data."""

        model = Contact
        fields = (
            "title",
            "full_name",
            "email",
            "phone_number",
            "message",
            "created_at",
        )


@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    """Configure the contact model in admin page."""

    resource_class = ContactResource

    date_hierarchy = "created_at"

    list_display = (
        "title",
        "full_name",
        "email",
    )

    ordering = (
        "title",
        "full_name",
        "email",
    )

    search_fields = ("title", "full_name", "email", "message", "phone_number")
