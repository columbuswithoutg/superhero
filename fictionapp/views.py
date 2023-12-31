from django.shortcuts import render
from .models import Hero, Comic, Type


def index(request):
    return render(request, 'index.html', {})


def hero_list(request):
    heroes = Hero.objects.all()
    return render(request, 'hero_list.html', {'heroes': heroes})

def comic_list(request):
    comics = Comic.objects.all()
    return render(request, 'comic_list.html', {'comics': comics})

def dc_list(request):
    heroes = Hero.objects.all()
    return render(request, 'dc_list.html', {'heroes': heroes})

def marvel_list(request):
    heroes = Hero.objects.all()
    return render(request, 'marvel_list.html', {'heroes': heroes})

def anime_list(request):
    heroes = Hero.objects.all()
    return render(request, 'anime_list.html', {'heroes': heroes})

def liveaction_list(request):
    heroes = Hero.objects.all()
    return render(request, 'liveaction_list.html', {'heroes': heroes})

def villain_list(request):
    villain_heroes = Hero.objects.filter(type__name='Villain')
    return render(request, 'villain_list.html', {'villain_heroes': villain_heroes})

def heroes_list(request):
    heroes = Hero.objects.filter(type__name='Hero')
    return render(request, 'heroes_list.html', {'heroes': heroes})

def antihero_list(request):
    heroes = Hero.objects.filter(type__name='Antihero')
    return render(request, 'antihero_list.html', {'heroes': heroes})

def type_list(request):
    types = Type.objects.all()
    return render(request, 'type_list.html', {'types': types})