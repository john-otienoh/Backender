from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *


# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"msg": "You registered successfuly!"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    if request.method == "GET":
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def update_profile(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    if request.method == "GET":
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
