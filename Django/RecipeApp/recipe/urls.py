from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/',login, name='login'),
    path('logout/', logout, name='logout'),
    # CRUD Operations
    path('', RecipeList.as_view(), name='recipe_list'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
]
