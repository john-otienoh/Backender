from .views import BookListView
from django.urls import path


app_name = "books"
urlpatterns = [path("", BookListView.as_view(), name="home")]
