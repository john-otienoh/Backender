from django.contrib import admin
from .models import CustomUser, BlogPost
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ["username", 'bio', 'facebook', 'twitter', 'gender', 'instagram', 'youtube', 'avatar']
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'publish', 'status', 'category']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
