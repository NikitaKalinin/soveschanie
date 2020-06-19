from django.urls import path
from . import views
#from .views import RoomList

urlpatterns = [
    path('', views.index, name='index'),
    #path('', RoomList.as_view(), name='RoomList-view'),
]