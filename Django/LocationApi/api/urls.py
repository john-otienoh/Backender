from django.urls import path
from .views import LocationDetail, LocationList

urlpatterns = [
    path("", LocationList.as_view(), name='location-list'),
    path("<int:pk>/", LocationDetail.as_view(), name='location-detail'),
]
