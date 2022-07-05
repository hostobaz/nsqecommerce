# modules
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

# models
from schools.models import Schools
from students.models import Students

# serializer student
from students.SerializerStudents import StudentSerializer

class ViewStudents(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Students.objects.all().order_by('-firstname')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]