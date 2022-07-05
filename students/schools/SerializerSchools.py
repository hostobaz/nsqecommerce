# modules
from rest_framework import serializers

# models
from schools.models import Schools
from students.models import Students

class SerializerSchools(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schools
        fields = ['url', 'name', 'max_number']

class SerializerStudentCreates(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['firstname','lastname']