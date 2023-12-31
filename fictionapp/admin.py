from django.contrib import admin
from .models import Hero, Comic, Type, Team
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = ['hero_name', 'civilian_name', 'email', 'birth_date', 'cinema_debut', 'comic', 'display_types']

    def display_types(self, obj):
        return ", ".join([type.name for type in obj.type.all()])

admin.site.register(Hero, HeroAdmin)
admin.site.register(Comic)
admin.site.register(Type)
admin.site.register(Team)
