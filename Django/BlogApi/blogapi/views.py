from django.shortcuts import render
from .serializers import (
    UserRegistrationSerializer,
    UserProfileSerializer,
    BlogPostSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
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
    try:
        user = CustomUser.objects.get(id=pk)

    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


@api_view(["PUT", "GET"])
@permission_classes([IsAuthenticated])
def update_profile(request, pk):
    user = CustomUser.objects.get(id=pk)
    if request.method == "GET":
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user = request.user
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def blog_list(request):
    blogs = BlogPost.objects.all()
    serializer = BlogPostSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def blog_detail(request, pk):
    try:
        blog = BlogPost.objects.get(id=pk)
    except BlogPost.DoesNotExist:
        return Response(
            {"message": "Seems the blog does not exist!"},
            status=status.HTTP_404_NOT_FOUND,
        )

    # GET - Retrieve blog details (for viewing/editing)
    if request.method == "GET":
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)


@api_view(["PUT", "GET"])
@permission_classes([IsAuthenticated])
def update_blog(request, pk):

    user = request.user
    blog = BlogPost.objects.get(id=pk)
    if request.method == "GET":
        # Return prefilled data for editing
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)

    if request.method == "PUT":
        if blog.author != user:
            return Response(
                {"error": "you are not the blog owner"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = BlogPostSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_blog(request, pk):
    user = request.user
    blog = BlogPost.objects.get(id=pk)
    if blog.author != user:
        return Response(
            {"error": "you are not the blog owner"}, status=status.HTTP_403_FORBIDDEN
        )
    blog.delete()
    return Response(
        {"message": "Blog deleted successfuly!"}, status=status.HTTP_204_NO_CONTENT
    )
