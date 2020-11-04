from django.shortcuts import render
from django.utils.html import mark_safe


from .models import Jogos, BlogPost

# Create your views here.

def index(request):
    return render(request, "games/index.html",{
        "jogos":Jogos.objects.all()
    })

   

def games_list(request):
    return render(request, "games/games_list.html",{
        "jogos": Jogos.objects.all()
    })

def jogo(request, jogo_id):
    jogo = Jogos.objects.get(pk=jogo_id)
    return render(request, "games/jogo.html",{
        "jogo": jogo,
        "generos": jogo.generos.all(),
        "plataformas": jogo.plataformas.all(),
        
    })
def news(request):
 
    qs = BlogPost.objects.all()
    template_name = 'games/news.html'
    context = {'object_list': qs}
    return render(request, template_name, context)