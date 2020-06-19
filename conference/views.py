from django.shortcuts import render

from django.views.generic import TemplateView
from proctorinterface.models import Room

'''
def index(request):
    return render(request, 'mainApp/conference-min.html')
'''
'''
class RoomList(TemplateView):
    template_name = 'conference.html'
    def get(self, request):
        all_room = Room.objects.all() #Все комнаты

        ctx = {
            'all_room': all_room,
        }
        return render(request, self.template_name, ctx)
'''
def index(request):
    rooms = Room.objects.all()
    return render(request, "mainApp/conference-min.html", {"rooms": rooms})