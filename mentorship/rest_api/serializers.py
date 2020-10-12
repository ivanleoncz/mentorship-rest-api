from rest_framework import serializers

from .models import Mentor, Project, Mentorship

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ('name', 'email')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name')

'''
class MentorshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ('name', 'email')
'''
