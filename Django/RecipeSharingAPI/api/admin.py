from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "chef",
        "title",
        "description",
        "servings",
        "slug",
        "cooking_time",
        "difficulty",
        "meal_type",
        "cuisine_type",
        "recipe_image",
        "category",
        "ingredients",
        "instructions",
        "id",
    ]
    list_filter = ["chef", "difficulty", "cuisine_type", "meal_type"]
    search_fields = ["chef", "title", "id"]
    # ordering = ["gender", "created"]
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    list_filter = ["name", "country"]
    show_facets = admin.ShowFacets.ALWAYS
