from django.db import models
from PIL import Image
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
import uuid

# Create your models here.


class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)


class Recipe(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "Easy", "Easy"
        MEDIUM = "Medium", "Medium"
        HARD = "Hard", "Hard"

    class MealType(models.TextChoices):
        BREAKFAST = "Breakfast", "Breakfast"
        BRUNCH = "Brunch", "Brunch"
        LUNCH = "Lunch", "Lunch"
        DINNER = "Dinner", "Dinner"
        DESSERT = "Dessert", "Dessert"
        BEVERAGES = "Beverages", "Beverages"
        OTHER = "Other", "Other"

    class Category(models.TextChoices):
        VEGETARIAN = "Vegetarian", "Vegetarian"
        GLUTEN_FREE = "Gluten Free", "GlutenFree"
        LOW_CARB = "Low Carb", "LowCarb"
        PALEO = "Paleo", "Paleo"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=50)
    chef = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipe_apis"
    )
    slug = models.SlugField(max_length=60, unique="id", blank=True)
    description = models.TextField()
    cooking_time = models.PositiveIntegerField(
        help_text="Total cooking time in minutes"
    )
    servings = models.IntegerField()
    difficulty = models.CharField(
        max_length=10, choices=Difficulty, default=Difficulty.EASY
    )
    cuisine_type = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True)
    meal_type = models.CharField(
        max_length=10, choices=MealType, default=MealType.OTHER
    )
    ingredients = models.CharField(max_length=1000)
    instructions = models.CharField(max_length=1000)
    category = models.CharField(
        max_length=20, choices=Category, default=Category.VEGETARIAN
    )
    recipe_image = models.ImageField(default="default.jpg", upload_to="recipe_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):

        return reverse("recipe_detail", args=[self.slug, self.id])
