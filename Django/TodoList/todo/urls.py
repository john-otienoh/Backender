from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_task, name="add_task"),
    path("delete/<int:task_id>/", views.delete, name="delete"),
]
