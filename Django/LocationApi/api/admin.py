from django.contrib import admin
from .models import Location


# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude", "address", "category"]
