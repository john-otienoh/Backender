from django.urls import path
from .views import *
from account.views import *

urlpatterns = [
    # User Management
    path("account/register/", register, name="register"),
    path("account/profile/<int:pk>/", profile, name="profile"),
    path("account/update_profile/<int:pk>/", update_profile, name="update_profile"),
    # Recipe Management
    path("recipes/", recipe_list, name="recipes_list"),
    path("recipes/create/", add_recipe, name="add_recipe"),
    path('recipes/search/', search, name='search'),
    path("recipes/<slug:recipe>/<uuid:pk>/", recipe_detail, name="recipe_detail"),
    path("recipes/edit/<slug:recipe>/<uuid:pk>", update_recipe, name="update_recipe"),
    path("recipes/delete/<slug:recipe>/<uuid:pk>", delete_recipe, name="delete_recipe"),
    # Community Interaction
]
