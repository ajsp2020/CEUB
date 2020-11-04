from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("games_list/", views.games_list, name="games_list"),
    path("games_list/<int:jogo_id>", views.jogo, name="jogo"),
    path("news/", views.news, name="news")
]
