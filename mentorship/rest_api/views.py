from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from .serializers import MentorSerializer, ProjectSerializer
from .models import Mentor, Project

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by('name')
    serializer_class = MentorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
