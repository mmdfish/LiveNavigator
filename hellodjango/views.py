from django.shortcuts import render

from django.shortcuts import HttpResponse
from hellodjango.models import LiveRoom
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def room_index(request):
    room_list = LiveRoom.objects.all()
    return render(request, 'room_index.html', {'room_list':room_list})