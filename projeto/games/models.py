from django.db import models

# Create your models here.

class Generos(models.Model):
    gen = models.CharField(max_length=64)

class Jogos(models.Model):
    
    nome = models.CharField(max_length=64)
    dataLancamento = models.IntegerField()
    plataforma = models.CharField(max_length=64)
    projetista = models.CharField(max_length=64)
    desenvolvedor = models.CharField(max_length=64)
    genero = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}, {self.desenvolvedor}"