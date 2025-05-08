from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type" "password"}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Your password and confirm password are not match"
            )
        return attrs

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "gender",
            "instagram",
            "twitter",
            "youtube",
            "facebook",
            "avatar",
            "bio",
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
        ]
