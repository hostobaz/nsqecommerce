# modules
from django.urls import path

# views
from schools.ViewSchools import ViewSchools, ViewStudentCreate
from students.ViewStudents import ViewStudents
# as views
as_view_schools_list = ViewSchools.as_view({
    'get': 'list',
    'post': 'create'
})

as_view_schools_detail = ViewSchools.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# as view for nested rout
as_view_schools_custom = ViewStudentCreate.as_view({
    'get': 'students_in_school',
    'post': 'students_in_school_create'
})

as_view_schools_specific = ViewStudents.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# urls
urlpatterns = [
    path('schools/', as_view_schools_list, name='schools-list'),
    path('schools/<int:pk>', as_view_schools_detail, name='schools-detail'),

    # neseted router
    path('schools/<int:pk>/students/', as_view_schools_custom, name='schools-custom'),
    path('schools/<int:school_id>/students/<int:pk>', as_view_schools_specific, name='nested-schools-detail'),
]