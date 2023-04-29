from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer

class WorkerListCreate(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
