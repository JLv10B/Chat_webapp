from django.shortcuts import render
from .models import Room

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'Front end'},
    {'id':3, 'name':'Back end'},
    {'id':4, 'name':'Full stack'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)