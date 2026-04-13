from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('pizza/<int:pk>/', views.pizza_detail, name='pizza_detail'),
    path('order/<int:pizza_pk>/', views.order_create, name='order_create'),
    path('orders/', views.order_list, name='order_list'),
]
