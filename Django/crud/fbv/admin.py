from django.contrib import admin
from .models import Employee

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "contact", "gender"]
    list_filter = ["gender", "created", "name"]
    search_fields = ["name"]
    ordering = ["gender", "created"]
    show_facets = admin.ShowFacets.ALWAYS
