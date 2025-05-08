from rest_framework import serializers
from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    recipe = Recipe()
    cuisine_type = serializers.SerializerMethodField()
    chef = serializers.SerializerMethodField()

    def get_cuisine_type(self, obj):
        return obj.cuisine_type.name if obj.cuisine_type else None

    def get_chef(self, obj):
        return obj.chef.username.capitalize() if obj.chef else None

    class Meta:
        model = Recipe
        fields = [
            "id",
            "chef",
            "title",
            "slug",
            "description",
            "servings",
            "cuisine_type",
            "meal_type",
            "difficulty",
            "recipe_image",
            "instructions",
            "ingredients",
            "cooking_time",
            "category",
        ]


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ["name", "country"]
