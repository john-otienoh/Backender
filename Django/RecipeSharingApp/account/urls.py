from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    
]
