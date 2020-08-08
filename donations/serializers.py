from rest_framework import serializers
from .models import Blood, Sponsor, Organ


class BloodDonationRequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blood
        fields = (
            "blood_type",
            "amount",
            "height",
            "weight",
            "last_donate_date",
            "has_hiv",
            "has_diabetes",
            "has_tattoo",
            "been_injured",
            "blood_transfusion",
            "been_in_prison",
            "feedback",
        )


class OrganDonationRequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organ
        fields = (
            "organ",
            "allergies",
            "medications",
            "has_disease",
            "has_asthma",
            "has_diabetes",
            "has_hypertension",
            "has_tuberculosis",
            "organ_date_registration",
        )


class MoneyDonationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sponsor

        fields = (
            "organization",
            "amount",
        )


class DonorSerializer(serializers.Serializer):

    username = serializers.CharField(read_only=True)

    picture = serializers.ImageField(read_only=True)


class RecentDonorsSerializer(serializers.Serializer):
    donor = DonorSerializer(read_only=True)

