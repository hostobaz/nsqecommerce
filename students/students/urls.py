# modules
from django.urls import path

# views
from .ViewStudents import ViewStudents

# as views
as_view_students_list = ViewStudents.as_view({
    'get': 'list',
    'post': 'create'
})

as_view_students_detail = ViewStudents.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# urls
urlpatterns = [
    path('students/', as_view_students_list, name='students-list'),
    path('students/<int:pk>', as_view_students_detail, name='students-detail'),
]