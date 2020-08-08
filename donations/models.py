"""Collection of model."""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class BloodType(models.TextChoices):
    """Enum class for blood type."""

    A = ("A", _("A"))

    A_PLUS = ("A+", _("A+"))

    A_MINUS = ("A-", _("A-"))

    AB = ("AB", _("AB"))

    B = ("B", _("B"))

    B_PLUS = ("B+", _("B+"))

    B_MINUS = ("B-", _("B-"))

    o = ("O", _("O"))

    o_PLUS = ("O+", _("O+"))

    o_MINUS = ("O-", _("O-"))


class Organization(models.TextChoices):
    """Enum class for organization type."""

    COVID = ("COVID-19", _("COVID-19"))

    MAKEDONIA = ("MAKEDONIA", _("MAKEDONIA"))

    SELE_ENAT_CHARITABLE = ("SELE ENAT CHARITABLE", _("SELE ENAT CHARITABLE"))


class OrgansChooses(models.TextChoices):
    """Enum class for organization type."""

    HEART = ("HEART", _("HEART"))

    KIDENY = ("KIDENY", _("KIDENY"))

    LIVER = ("LIVER", _("LIVER"))

    LUNG = ("LUNG", _("LUNG"))

    PANCREAS = ("PANCREAS", _("PANCREAS"))

    INTESTINES = ("INTESTINES", _("INTESTINES"))


class Blood(models.Model):
    """Reference blood model."""

    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("donor"),
        on_delete=models.CASCADE,
        related_name="bloods",
        db_index=True,
    )

    blood_type = models.CharField(choices=BloodType.choices, verbose_name=_("blood type"),
                                  max_length=5)

    amount = models.PositiveIntegerField(verbose_name=_("amount"))

    height = models.FloatField(verbose_name=_("height"))

    weight = models.FloatField(verbose_name=_("weight"))

    last_donate_date = models.DateField(verbose_name=_("last donate date"), null=True, blank=True)

    has_hiv = models.BooleanField(verbose_name=_("do you have hiv"), null=True, blank=True)

    take_drugs = models.BooleanField(verbose_name=_("do you use drugs"), null=True, blank=True)

    has_diabetes = models.BooleanField(verbose_name=_("do you use diabetes"), null=True, blank=True)

    has_tattoo = models.BooleanField(verbose_name=_("had a tattoo"), null=True, blank=True)

    been_injured = models.BooleanField(verbose_name=_("been injured with a used neddle"), null=True, blank=True)

    blood_transfusion = models.BooleanField(verbose_name=_("had a blood transfusion"), null=True, blank=True)

    been_in_prison = models.BooleanField(verbose_name=_("been imprisoned in a prison"), null=True, blank=True)

    feedback = models.TextField(verbose_name=_("feedback"), null=True, blank=True)

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("blood")
        verbose_name_plural = _("bloods")

    def __str__(self: "Blood") -> str:
        """It return readable name for the model."""
        return f"{self.donor}"


class Organ(models.Model):
    """Reference organ model."""

    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("donor"),
        on_delete=models.CASCADE,
        related_name="organs",
        db_index=True,
    )

    organ = models.CharField(choices=OrgansChooses.choices, verbose_name=_("organ"), max_length=200)

    allergies = models.BooleanField(verbose_name=_("allergies"), null=True, blank=True)

    medications = models.BooleanField(verbose_name=_("medications"), null=True, blank=True)

    has_disease = models.BooleanField(verbose_name=_("do you have a disease"), null=True, blank=True)

    has_asthma = models.BooleanField(verbose_name=_("do you have a asthma"), null=True, blank=True)

    has_diabetes = models.BooleanField(verbose_name=_("do you use diabetes"), null=True, blank=True)

    has_hypertension = models.BooleanField(verbose_name=_("do you have a hypertension"), null=True, blank=True)

    has_tuberculosis = models.BooleanField(verbose_name=_("do you have a tuberculosis"), null=True, blank=True)

    organ_date_registration = models.DateField(verbose_name=_("organ date registration"), null=True, blank=True)

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("organ")
        verbose_name_plural = _("organs")

    def __str__(self: "Organ") -> str:
        """It return readable name for the model."""
        return f"{self.donor}"


class Sponsor(models.Model):
    """Reference sponsor model."""

    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("donor"),
        on_delete=models.CASCADE,
        related_name="sponsors",
        db_index=True,
    )

    organization = models.CharField(choices=Organization.choices, verbose_name=_("blood type"), max_length=300)

    amount = models.PositiveIntegerField(verbose_name=_("amount"))

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("sponsor")
        verbose_name_plural = _("sponsors")

    def __str__(self: "Sponsor") -> str:
        """It return readable name for the model."""
        return f"{self.donor}"

