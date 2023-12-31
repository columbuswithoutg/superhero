# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hero_list.html', views.hero_list, name='hero_list'),
    path('comic_list.html', views.comic_list, name='comic_list'),
    path('dc_list.html', views.dc_list, name='dc_list'),
    path('marvel_list.html', views.marvel_list, name='marvel_list'),
    path('liveaction_list.html', views.liveaction_list, name='liveaction_list'),
    path('anime_list.html', views.anime_list, name='anime_list'),
    path('villain_list.html', views.villain_list, name='villain_list'),
    path('heroes_list.html', views.heroes_list, name='heroes_list'),
    path('antihero_list.html', views.antihero_list, name='antihero_list'),
    path('type_list.html', views.type_list, name='type_list'),
    path('team_list.html', views.team_list, name='team_list'),
    path('avengers_list.html', views.avengers_list, name='avengers_list'),
    path('justice_list.html', views.justice_list, name='justice_list'),
    path('noteam_list.html', views.noteam_list, name='noteam_list'),
    path('male_list.html', views.male_list, name='male_list'),
    path('female_list.html', views.female_list, name='female_list'),
    path('sex_list.html', views.sex_list, name='sex_list'),
]
