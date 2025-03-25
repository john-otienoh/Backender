from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique_for_date='posted')
    chef = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipes/', default='recipe.jpg')
    posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[self.posted.day, self.slug])
