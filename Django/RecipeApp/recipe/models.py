from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    """Custom User Model."""
    def __str__(self):
        return self.username
    
class Recipe(models.Model):
    "Model for Storing Recipes"
    title = models.CharField(max_length=50)
    chef = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe_image = models.ImageField()
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.IntegerField()
    
    def __str__(self):
        return self.title
    