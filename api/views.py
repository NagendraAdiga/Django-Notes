from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/task-list/',
        'Detail-view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    seralizer = TaskSerializer(task, many=False)
    return Response(seralizer.data)


@api_view(['POST'])
def taskCreate(request):
    serailizer = TaskSerializer(data=request.data)

    if serailizer.is_valid():
        serailizer.save()

    return Response(serailizer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serailizer = TaskSerializer(instance=task, data=request.data)

    if serailizer.is_valid():
        serailizer.save()

    return Response(serailizer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Task deleted')
