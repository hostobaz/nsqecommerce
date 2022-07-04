# modules
from rest_framework import serializers

# models
from students.models import Students

class SerializerStudentCreates(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['firstname','lastname']
