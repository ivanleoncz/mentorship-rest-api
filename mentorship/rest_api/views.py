from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
from .serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer
from .models import Mentor, Project, Mentorship

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by('id')
    serializer_class = MentorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

class MentorshipViewset(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all().order_by('id')
    serializer_class = MentorshipSerializer

    def create(self, request, *args, **kwargs):

        data = request.data
        if Mentor.objects.filter(name=data["mentor"]).count() == 0:
            return Response({'status': 'mentor not found'},
                                            status=status.HTTP_404_NOT_FOUND)

        if Project.objects.filter(name=data["project"]).count() == 0:
            return Response({'status': 'project not found'},
                                            status=status.HTTP_404_NOT_FOUND)

        new_mentorship = Mentorship.objects.create(
            mentor=Mentor.objects.get(name=data["mentor"]),
            project=Project.objects.get(name=data["project"])
        )
        new_mentorship.save()

        serializer = MentorshipSerializer(new_mentorship)

        return Response(serializer.data)
