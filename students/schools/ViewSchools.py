# modules
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.urls import include

# models
from schools.models import Schools
from students.models import Students

# serializer schools
from schools.SerializerSchools import SerializerSchools, SerializerStudentCreates

# class school manage
from schools.SchoolManage import SchoolManage

# view default schools
class ViewSchools(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited.
    """
    queryset = Schools.objects.all()
    serializer_class = SerializerSchools
    permission_classes = [permissions.IsAuthenticated]

# view students create
class ViewStudentCreate(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Students.objects.all().order_by('-firstname')
    serializer_class = SerializerStudentCreates
    permission_classes = [permissions.IsAuthenticated]

    def students_in_school(self, request, pk):
        # check school is exists
        get_data_school = SchoolManage.checkSchoolExists(Schools, pk, 'all')
        if get_data_school == None:
            return Response({ 'data': {}, 'message':'School is not found'}, status=status.HTTP_400_BAD_REQUEST)

        students_in_school = Students.objects.filter(school_id=pk).values()
        return Response({'data': students_in_school, 'message': 'Retrieve Successfully'}, status=status.HTTP_200_OK)
        
    def students_in_school_create(self, request, pk):
        # check if parameter sent completely
        serializer_student = SerializerStudentCreates(data=request.data)
        if serializer_student.is_valid():
            input_serializer_student = serializer_student.data
        else:
            return Response({'data': [], 'message':'Your input is not sent completely. ', 'status': status.HTTP_400_BAD_REQUEST })

        # preparing input
        get_input_list = {
            "school_id": pk,
            "firstname":  str(input_serializer_student['firstname']),
            "lastname": str(input_serializer_student["lastname"])
        }

        # check school is exists
        get_data_school = SchoolManage.checkSchoolExists(Schools, get_input_list["school_id"], 'all')
        if get_data_school == None:
            return Response({ 'data': {}, 'message':'School is not found'}, status=status.HTTP_400_BAD_REQUEST)

        # max_number and school name
        max_number = int(get_data_school["max_number"])
        school_name = str(get_data_school["name"])
        # number of students
        total_number = SchoolManage.checkSchoolExists(Students, get_input_list["school_id"], 'student_count')

        # detected is school full?
        if max_number <= total_number:
            return Response({ 'data': {}, 'message': f'Student in {school_name} is full'}, status=status.HTTP_400_BAD_REQUEST)

        # create Students
        Students.objects.create(
            firstname=get_input_list["firstname"],
            lastname=get_input_list["lastname"],
            school_id=get_input_list["school_id"]
            )
            
        return Response({'data': {}, 'message': 'Create student'}, status=status.HTTP_201_CREATED)