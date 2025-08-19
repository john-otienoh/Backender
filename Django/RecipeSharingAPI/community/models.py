from django.db import models
from django.conf import settings
from api.models import Recipe

# Create your models here.
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_apis"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ['created_at'] 
        indexes = [ models.Index(fields=['created_at']), ]
        
    def __str__(self): 
        return f'Comment by {self.user} on {self.recipe}'
          