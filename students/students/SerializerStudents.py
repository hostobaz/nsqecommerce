# modules
from rest_framework import serializers

# models
from students.models import Students

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['url', 'firstname','lastname','school']