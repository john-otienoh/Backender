from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("<int:post_id>/share/", views.post_share, name="share"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="detail",
    ),
    path("search/", views.post_search, name="search"),
    path("feed/", LatestPostsFeed(), name="feed"),
    path("<int:post_id>/comment/", views.post_comment, name="comment"),
]
