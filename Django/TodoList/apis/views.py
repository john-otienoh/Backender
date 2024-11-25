from rest_framework import generics
from todo.models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
