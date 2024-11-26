from rest_framework import serializers
from django.contrib.auth import get_user_model
from aviblogs.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
            "updated",
            "status",
            "publish",

        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username"
        )
