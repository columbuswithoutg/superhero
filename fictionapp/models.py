from django.db import models
from datetime import datetime, date
from django.core.validators import EmailValidator

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Comic(BaseModel):
    class ComicChoices(models.TextChoices):
        DC = 'DC', 'DC'
        MARVEL = 'Marvel', 'Marvel'
        ANIME = 'Anime', 'Anime'
        LIVE_ACTION = 'Live Action', 'Live Action'

    name = models.CharField(max_length=100, choices=ComicChoices.choices)

    def __str__(self):
        return self.name
    

class Type(BaseModel):
    class TypeChoices(models.TextChoices):
        VILLAIN = 'Villain', 'Villain'
        HERO = 'Hero', 'Hero'
        ANTIHERO = 'Antihero', 'Antihero'

    name = models.CharField(max_length=50, choices=TypeChoices.choices)

    def __str__(self):
        return self.name
    
class Team(BaseModel):
    class TeamChoices(models.TextChoices):
        AVENGERS = 'Avengers', 'Avengers'
        JUSTICELEAGUE = 'Justice League', 'Justice League'
        NOTEAM = 'No Team', 'No Team'

    name = models.CharField(max_length=50, choices=TeamChoices.choices, null=True, blank=True)

    def __str__(self):
        return self.name
class Sex(BaseModel):
    class SexChoices(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'

    name = models.CharField(max_length=50, choices=SexChoices.choices)

    def __str__(self):
        return self.name

class Hero(BaseModel):
    hero_name = models.CharField(max_length=200, default='Unknown')
    civilian_name = models.CharField(max_length=200, default='Unknown')
    email = models.CharField(max_length=255, validators=[EmailValidator], default='default@example.com')
    birth_date = models.DateField(default=date(2020, 6, 8))
    cinema_debut = models.DateTimeField(default=datetime(2020, 6, 8))
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    type  = models.ManyToManyField(Type)
    sex  = models.ManyToManyField(Sex)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.hero_name



