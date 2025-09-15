from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("update_profile/<int:pk>/", update_profile, name="update_profile"),
    # CRUD FUNCTIONS
    path("create/", create_blog, name="create"),
    path("list/", blog_list, name="list"),
    path("detail/<int:pk>/", blog_detail, name="detail"),
    path("update/<int:pk>/", update_blog, name="update"),
    path("delete/<int:pk>/", delete_blog, name="delete"),
]
