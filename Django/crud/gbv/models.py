from django.db import models
from django.urls import reverse


# Create your models here.
class Employee(models.Model):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Other"

    name = models.CharField(max_length=50)
    employee_number = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    contact = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender, default=Gender.OTHER)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["-updated"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gbv:detail", kwargs={"pk": self.pk})
