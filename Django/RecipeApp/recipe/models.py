from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    """Custom User Model."""
    def __str__(self):
        return self.username
    