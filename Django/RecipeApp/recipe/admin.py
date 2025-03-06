from django.contrib import admin
from .models import CustomUser, Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    "Display Recipe Model in the Admin Page."
    list_display = ['title', 'chef', 'recipe_image', 'servings']
    list_filter = ['title', 'chef']
    search_fields = ['title']
    # prepopulated_fields = {'slug': ('title',)}
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    "Display CustomUser Model in the Admin Page."
    show_facets = admin.ShowFacets.ALWAYS
