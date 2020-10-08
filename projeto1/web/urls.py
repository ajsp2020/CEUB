from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path('', views.index, name="index"),
    path("videos/", views.videos, name="videos"),
    path("dadosgerais", views.dadosgerais, name="dadosgerais"),
    path("sections/<int:num>", views.section, name="section"),
    path("descricaov2/", views.descricaov2, name= "descricaov2"),
    path("metodologia/", views.metodologia, name="metodologia"),
    path("arquitetura/", views.arquitetura, name="arquitetura"),
    path("descricao/", views.descricao, name="descricao"),
    path("descricao2/", views.descricao2, name="descricao2"),
    path("comentarios/", views.comentarios, name= "comentarios")
]