from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Task


# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})


@require_http_methods(["POST"])
def add_task(request):
    title = request.POST.get("title")
    if title:
        Task.objects.create(title=title)
    return redirect("todo:home")


# @require_http_methods(['POST'])
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("todo:home")
