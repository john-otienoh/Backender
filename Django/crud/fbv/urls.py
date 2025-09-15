from django.urls import path
from . import views

app_name = "fbv"
urlpatterns = [
    path("list/", views.list, name="list"),
    path("create/", views.create, name="create"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("search/", views.search, name="search"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("delete/<int:id>/", views.delete, name="delete"),
]
