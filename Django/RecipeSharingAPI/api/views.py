from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from .models import *


# Create your views here.
# @api_view(["GET"])
# def cuisine_list(request):
#     cuisines = Cuisine.objects.all()
#     serializer = CuisineSerializer(cuisines, many=True)
#     return Response(serializer.data)


@api_view(["GET"])
def recipe_list(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def recipe_detail(request, recipe, pk):
    recipe = get_object_or_404(Recipe, slug=recipe, id=pk)
    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)


@api_view(["POST"])
def add_recipe(request):
    user = request.user
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(chef=user)
        return Response({"message": "Recipe created successfully"}, serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "GET"])
def update_recipe(request, pk):
    user = request.user
    recipe = Recipe.objects.get(id=pk)
    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    if request.method == "PUT":
        if recipe.chef != user:
            return Response(
                {"error": "you are not the recipe owner"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {"message": "Recipe edited successfully"},
            serializer.errors,
            status=status.HTTP_403_FORBIDDEN,
        )


@api_view(["POST"])
def delete_recipe(request, pk):
    user = request.user
    recipe = Recipe.objects.get(id=pk)
    if recipe.chef != user:
        return Response(
            {"error": "you are not the recipe owner"},
            status=status.HTTP_403_FORBIDDEN,
        )
    recipe.delete()
    return Response(
        {"message": "Recipe deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )


@api_view(["GET"])
def search(request, query=None):

    search_query = query or request.GET.get("q", "").strip()
    if not search_query:
        return Response(
            {"error": "Please provide a search query"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    results = Recipe.objects.filter(
        Q(title__icontains=search_query) | Q(chef__username__icontains=search_query)
    ).distinct()
    if not results.exists():
        return Response(
            {
                "message": f"No recipes or chef's found matching '{search_query}'",
            },
            status=status.HTTP_200_OK,
        )

    serializer = RecipeSerializer(results, many=True)
    return Response(
        # {"count": results.count(), "results": serializer.data},
        # status=status.HTTP_200_OK,
        serializer.data
    )
