from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("inicial/", views.inicial, name="inicial")
]