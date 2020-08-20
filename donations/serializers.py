from rest_framework import serializers
from .models import Blood, Sponsor, Organ, Acceptor


class BloodDonationRequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blood
        fields = (
            "blood_type",
            "code",
            "number",
            "country",
            "city",
            "amount",
            "height",
            "weight",
            "last_donate_date",
            "has_hiv",
            "has_diabetes",
            "has_tattoo",
            "take_drugs",
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
            "country",
            "city",
            "code",
            "number",
            "allergies",
            "medications",
            "has_disease",
            "has_asthma",
            "has_diabetes",
            "has_hypertension",
            "has_tuberculosis",
            "has_cardiovascular",
            "has_transplants",
            "has_education",
            "organ_date_registration",
        )


class MoneyDonationSerializer(serializers.ModelSerializer):
    organization = serializers.ChoiceField(("COVID-19", "MAKEDONIA", "SELE ENAT CHARITABLE", "ETHIOPIAN CENTER FOR DISABILITY AND DEVLOPMENT"), required=False)

    class Meta:

        model = Sponsor

        fields = (
            "organization",
            "users",
            "amount",
            "fixed_amount",
            "country",
            "city",
            "code",
            "number",
        )


class DonorSerializer(serializers.Serializer):

    username = serializers.CharField(read_only=True)

    picture = serializers.ImageField(read_only=True)


class RecentDonorsSerializer(serializers.Serializer):
    donor = DonorSerializer(read_only=True)


class AcceptorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acceptor
        fields = ("name", "picture", "id")
