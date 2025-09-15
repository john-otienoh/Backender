from django.db import models

# from django.contrib.gis.db import models


class Location(models.Model):
    """Stores a location."""

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.name
