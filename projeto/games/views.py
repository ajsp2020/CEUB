from django.shortcuts import render

from .models import Jogos

# Create your views here.

def index(request):
    return render(request, "games/index.html")

def games_list(request):
    return render(request, "games/games_list.html",{
        "jogos": Jogos.objects.all()
    })

def jogo(request, jogo_id):
    jogo = Jogos.objects.get(pk=jogo_id)
    return render(request, "games/jogo.html",{
        "jogo": jogo,
        "generos": jogo.generos.all(),
        "plataformas": jogo.plataformas.all()
    })