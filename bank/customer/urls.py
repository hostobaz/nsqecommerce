# modules
from django.urls import path

#views
from .ViewCustomer import ViewCustomer

# set lists
customer_list = ViewCustomer.as_view({
    'get': 'list',
    'post': 'create'
})

# set details
customer_detail = ViewCustomer.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# urls
urlpatterns = [
    path('customer/', customer_list, name='customer-list'),
    path('customer/<int:pk>', customer_detail, name='customer-detail'),
]