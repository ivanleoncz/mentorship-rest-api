from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from .serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer
from .models import Mentor, Project, Mentorship

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by('name')
    serializer_class = MentorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer

class MentorshipViewset(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all().order_by('status')
    serializer_class = MentorshipSerializer