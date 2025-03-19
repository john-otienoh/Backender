from django.contrib import admin
from .models import Profile, Recipe
# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'chef', 'description', 'cuisine']
    search_fields = ['title', 'chef', 'cuisine']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['chef']
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Profile)
