from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

from rest_framework.views import APIView #probando apis
from rest_framework.response import Response #probando apis

#class TaskViewSet(viewsets.ModelViewSet):
#    queryset = Task.objects.all()
#    serializer_class = TaskSerializer
    

class HelloWorldView(APIView): #clase para probar apis
    def get(self, request):
        return Response({"message": "Hello from Django REST Framework!"})