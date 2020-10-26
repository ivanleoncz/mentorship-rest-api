from rest_framework import serializers

from .models import Mentor, Project, Mentorship

class MentorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mentor
        fields = ('id', 'name', 'email')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name',)

class MentorshipSerializer(serializers.ModelSerializer):

    mentor = serializers.CharField(source="mentor.name", read_only=True)
    project = serializers.CharField(source="project.name", read_only=True)

    class Meta:
        model = Mentorship
        fields = ('id', 'mentor', 'project', 'status')

