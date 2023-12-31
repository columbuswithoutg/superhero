from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Hero, Comic, Type, Team, Sex


def index(request):
    return render(request, 'index.html', {})


def hero_list(request):
    myheroes = Hero.objects.all()
    p = Paginator(myheroes, 5)
    page = request.GET.get('page')
    heroes = p.get_page(page)
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

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def avengers_list(request):
    avengers_teams = Team.objects.filter(name='Avengers')
    avengers_heroes = Hero.objects.filter(team__in=avengers_teams)
    return render(request, 'avengers_list.html', {'avengers_heroes': avengers_heroes})

def justice_list(request):
    justice_league_team = Team.objects.filter(name='Justice League')
    justice_league_heroes = Hero.objects.filter(team__in=justice_league_team)
    return render(request, 'justice_list.html', {'justice_league_heroes': justice_league_heroes})

def noteam_list(request):
    no_team_team = Team.objects.filter(name='No Team')
    no_team_heroes = Hero.objects.filter(team__in=no_team_team)
    return render(request, 'no_team_list.html', {'no_team_heroes': no_team_heroes})

def male_list(request):
    male_team = Sex.objects.filter(name='Male')
    male_heroes = Hero.objects.filter(sex__in=male_team)
    return render(request, 'male_list.html', {'male_heroes': male_heroes})

def female_list(request):
    female_team = Sex.objects.filter(name='Female')
    female_heroes = Hero.objects.filter(sex__in=female_team)
    return render(request, 'female_list.html', {'female_heroes': female_heroes})

def sex_list(request):
    sex = Sex.objects.all()
    return render(request, 'sex_list.html', {'sex': sex})