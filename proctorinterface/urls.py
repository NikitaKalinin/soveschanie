from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_room/', views.create_room, name='create_room'),
    path('delete_room/', views.delete_room, name='delete_room'),
]
