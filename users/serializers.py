from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from .models import CustomUser
from .validators import validate_confusables, validate_confusables_email, validate_reserved_name


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

        username = validated_data.get("username")

        email = validated_data.get("email")

        local, domain = email.split("@")

        validate_reserved_name(value=username, exception_class=exceptions.ValidationError)

        validate_reserved_name(value=local, exception_class=exceptions.ValidationError)

        validate_confusables(value=username, exception_class=exceptions.ValidationError)

        validate_confusables_email(local_part=local, domain=domain, exception_class=exceptions.ValidationError)

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
            "total_blood_amount",
            "total_money_amount",
            "list_of_organs",
        )


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("username", "picture", "id")


class UserPictureUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("picture",)


class UserChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(style={"input_type": "password"})

    new_password = serializers.CharField(style={"input_type": "password"})

    retype_new_password = serializers.CharField(style={"input_type": "password"})

    def validate_new_password(self, password: str):

        validate_password(password=password)

        return super(UserChangePasswordSerializer, self).validate(password)
