"""Core app for users app."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactConfig(AppConfig):
    """Class representing a Django application and its configuration."""

    name = "contact"
    verbose_name = _("contact")
