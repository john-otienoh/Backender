from django.db import models
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    published = models.DateTimeField(timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
