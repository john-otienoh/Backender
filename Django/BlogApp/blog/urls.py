from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.post_list, name='list'),
    path('blog/<int:id>/', views.post_detail, name='detail'),
]
