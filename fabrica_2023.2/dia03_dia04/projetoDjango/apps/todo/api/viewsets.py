from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    
    # quero todos osd dados que estao na tabela task
    queryset = Task.objects.all() #-> chamada para o banco de dados
    
    serializer_class = TaskSerializer