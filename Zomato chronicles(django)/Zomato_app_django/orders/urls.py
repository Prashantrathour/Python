from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('take_order', views.take_order, name='take_order'),
    # path('orders', views.orders, name='orders'),
]