from rest_framework import serializers
from .models import Request, Sponsor


class BloodDonationRequestsSerializer(serializers.ModelSerializer):

    class Meta:
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
        )


class OrganDonationRequestsSerializer(serializers.ModelSerializer):

    class Meta:
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
            "height",
            "weight",
            "blood_pressure",
            "allergies",
            "medical_conditions",
            "organ_date_registration",
            "organs_to_be_donated",
        )


class MoneyDonationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sponsor

        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "country",
            "city",
            "amount",
        )
