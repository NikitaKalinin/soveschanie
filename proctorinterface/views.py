from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Room
from .forms import RoomForm

def index(request):
    #form = RoomForm(request.POST or None)

    #if request.method == "POST" and form.is_valid():
        #print(form.cleaned_data)
    return render(request, 'mainApp/proctorinterface.html', locals())

def create_room(request):
    form = RoomForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        proctor_id = request.POST['proctor_id']
        description = request.POST['description']
        name = request.POST['name']
        #print(request.POST)
        form.save()
    #print(form.errors)
    return HttpResponse('OK')

def delete_room(request):
    try:
    #field1 = request.POST['proctor_id']
    #field2 = request.POST['description']
        field3 = request.POST['name']
        room = Room.objects.get(name=field3)
        room.delete()
        #return HttpResponse("OK")
        return HttpResponseRedirect("/")
    except Room.DoesNotExist:
        #return HttpResponse("OK")
        return HttpResponseNotFound("<h2>Room is not found</h2>")