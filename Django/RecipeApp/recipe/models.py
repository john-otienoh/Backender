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
    recipe_image = models.ImageField(upload_to='recipe_images', blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.IntegerField()

    def get_total_number_of_bookmarks(self):
        return self.bookmarked_by.count()
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    bookmarks = models.ManyToManyField('Recipe', related_name='bookmarked_by')
    def __str__(self):
        return self.user.username
    
class Save(models.Model):
    """
    Model to save recipes
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarks')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='bookmarks')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
    def __str__(self):
        return f"{self.user.username} bookmarked {self.recipe.title}"
        