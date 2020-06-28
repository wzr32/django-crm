from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('customer/<str:id>', customer, name='customer'),
    path('create_order/<str:id>', create_order, name='create_order'),
    path('update_order/<str:id>', update_order, name='update_order'),
    path('delete_order/<str:id>', delete_order, name='delete_order')
]
