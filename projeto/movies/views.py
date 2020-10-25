from django.shortcuts import render
from .models import Filmes

# Create your views here.
def index(request):
    return render (request, "movies/index.html",{
        "movies":Filmes.objects.all()
    })

def inicial(request):
    return render (request, "movies/inicial.html")