# modules
from rest_framework import serializers

# models
from schools.models import Schools

class SerializerSchools(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schools
        fields = ['url', 'name', 'max_number']


