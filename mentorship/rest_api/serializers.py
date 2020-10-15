from rest_framework import serializers

from .models import Mentor, Project, Mentorship

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ('name', 'email')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name',)

class MentorshipSerializer(serializers.ModelSerializer):
    mentor = serializers.CharField(source="mentor_id")
    project = serializers.CharField(source="project_id")
    class Meta:
        model = Mentorship
        fields = ('id', 'mentor', 'project', 'status')
