from django.contrib import admin

# Register your models here.
from . models import Jogos, Generos, Plataformas, Fotos

admin.site.register(Jogos)
admin.site.register(Generos)
admin.site.register(Plataformas)
admin.site.register(Fotos)