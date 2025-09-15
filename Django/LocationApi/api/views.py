from django.shortcuts import render
from rest_framework import generics, status
from .models import Location
from .serializers import LocationSerializer

# Create your views here.


class LocationList(generics.ListCreateAPIView):
    """List all locations."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveAPIView):
    """Get specific location details"""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
