from django.urls import path
from . import views

app_name = "gbv"

urlpatterns = [
    path("list/", views.EmployeeListView.as_view(), name="list"),
    path("create/", views.EmployeeCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", views.EmployeeUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", views.EmployeeDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", views.EmployeeDetailView.as_view(), name="detail"),
]
