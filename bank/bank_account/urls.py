# modules
from django.urls import path

#views
from .ViewBankAccount import ViewBankAccount

# set lists
bank_account_list = ViewBankAccount.as_view({
    'get': 'list',
    'post': 'create'
})

# set details
bank_account_detail = ViewBankAccount.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# urls
urlpatterns = [
    path('account/', bank_account_list, name='bankaccount-list'),
    path('account/<int:pk>', bank_account_detail, name='bankaccount-detail'),
]