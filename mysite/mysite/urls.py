from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('userinterface/', include('userinterface.urls')),
    path('userinstruction/', include('userinstruction.urls')),
    path('connecting/', include('connecting.urls')),
    path('signin/', include('signin.urls')),
    path('conference/', include('conference.urls')),
    path('proctorinterface/', include('proctorinterface.urls')),
]
