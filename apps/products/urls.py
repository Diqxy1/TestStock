from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
]
