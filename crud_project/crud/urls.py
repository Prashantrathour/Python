from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:item_id>/', views.update, name='update'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]