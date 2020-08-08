from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    """Reference contact model."""

    title = models.CharField(verbose_name=_("title"), max_length=100)

    full_name = models.CharField(verbose_name=_("full name"), max_length=300)

    email = models.EmailField(verbose_name=_("email address"), unique=True)

    phone_number = models.CharField(verbose_name=_("phone number"), max_length=15)

    message = models.TextField(verbose_name=_("message"))

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self: "Contact") -> str:
        """It return readable name for the model."""
        return f"{self.title}"

