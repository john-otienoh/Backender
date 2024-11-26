from . import views
from django.urls import path, include

app_name = 'aviblogs'

urlpatterns = [
    path( 'tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag' ),
    path('', views.PostList.as_view(),name='post_list' ),
    path( '<int:post_id>/comment/', views.post_comment, name='post_comment' ),
]