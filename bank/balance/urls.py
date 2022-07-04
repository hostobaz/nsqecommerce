# modules
from django.urls import path

#views
from .ViewBalance import ViewBalance

# set views
view_transaction = ViewBalance.as_view({
    'get': 'view_transaction'
})

create_transaction = ViewBalance.as_view({
    'post': 'create_transaction'
})

view_balance = ViewBalance.as_view({
    'get': 'view_balance'
})

# urls
urlpatterns = [
    path('transaction/<int:bankId>', view_transaction, name='transfer-view'),
    path('transfer/add/<int:bankId>', create_transaction, name='transfer-create'),
    path('balance/<int:bankId>', view_balance, name='view_balance-get'),
]