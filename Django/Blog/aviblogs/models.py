from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        """Manages status of our blog post"""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='casa_posts')
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)
    tags = TaggableManager()

    class Meta:
        """Metadata for the model"""
        ordering = ['-publish']
        indexes = [ models.Index(fields=['-publish']), ]

    def get_absolute_url(self):
        return reverse("casa:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [ 
            models.Index(fields=['created']), 
        ]
        def __str__(self):
            return f'Comment by {self.name} on {self.post}'
        
