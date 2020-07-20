"""Collection of model."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class BloodType(models.TextChoices):
    """Enum class for blood type."""

    A = ("A", _("A"))

    AB = ("AB", _("AB"))

    B = ("B", _("B"))

    o = ("O", _("O"))


class Request(models.Model):
    """Reference request model."""

    first_name = models.CharField(verbose_name=_("first name"), max_length=300)

    last_name = models.CharField(verbose_name=_("last name"), max_length=300)

    email = models.EmailField(verbose_name=_("email address"), unique=True)

    phone_number = models.CharField(verbose_name=_("phone number"), max_length=15)

    country = models.CharField(verbose_name=_("country"), max_length=100)

    city = models.CharField(verbose_name=_("city"), max_length=100)

    date_of_birth = models.DateField(verbose_name=_("date of birth"))

    blood_type = models.CharField(choices=BloodType.choices, verbose_name=_("blood type"), null=True, blank=True, max_length=5)

    message = models.TextField(verbose_name=_("message"), null=True, blank=True)

    height = models.FloatField(verbose_name=_("height"), null=True, blank=True)

    weight = models.FloatField(verbose_name=_("weight"), null=True, blank=True)

    blood_pressure = models.FloatField(verbose_name=_("blood pressure"), null=True, blank=True)

    allergies = models.CharField(verbose_name=_("allergies"), null=True, blank=True, max_length=200)

    medical_conditions = models.CharField(verbose_name=_("medical conditions"), null=True, blank=True, max_length=300)

    organ_date_registration = models.DateField(verbose_name=_("organ date registration"), null=True, blank=True)

    organs_to_be_donated = models.TextField(verbose_name=_("organs to be donated"), null=True, blank=True)

    is_accepted = models.BooleanField(verbose_name=_("is accepted"), null=True, blank=True)

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("request")
        verbose_name_plural = _("requests")

    def __str__(self: "Request") -> str:
        """It return readable name for the model."""
        return f"{self.first_name} {self.last_name}"


class Sponsor(models.Model):
    """Reference sponsor model."""

    first_name = models.CharField(verbose_name=_("first name"), max_length=300)

    last_name = models.CharField(verbose_name=_("last name"), max_length=300)

    email = models.EmailField(verbose_name=_("email address"), unique=True)

    phone_number = models.CharField(verbose_name=_("phone number"), max_length=15)

    country = models.CharField(verbose_name=_("country"), max_length=100)

    city = models.CharField(verbose_name=_("city"), max_length=100)

    amount = models.PositiveIntegerField(verbose_name=_("amount"))

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("sponsor")
        verbose_name_plural = _("sponsors")

    def __str__(self: "Sponsor") -> str:
        """It return readable name for the model."""
        return f"{self.first_name} {self.last_name} Sponsor {self.amount}"

