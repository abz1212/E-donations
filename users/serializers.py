from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
            "email",
            "full_name",
            "country",
            "city",
            "picture",
            "phone_number",
            "date_of_birth",
        )
        extra_kwargs = {'password': {'write_only': True, "style": {"input_type": "password"}}}

    def validate_password(self, value):
        validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "country",
            "city",
            "picture",
            "phone_number",
            "date_of_birth",
        )
