from django.db import models

# Create your models here.



class Jogos(models.Model):
    
    nome = models.CharField(max_length=64)
    dataLancamento = models.IntegerField()
    projetista = models.CharField(max_length=64,blank=True)
    desenvolvedor = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id}: {self.nome}, {self.desenvolvedor}"

class Generos(models.Model):
    gen = models.CharField(max_length=64)
    games = models.ManyToManyField(Jogos, blank=True, related_name="generos")

    def __str__(self):
        return f"{self.gen}"

class Plataformas(models.Model):
    plataforma = models.CharField(max_length=64)
    games = models.ManyToManyField(Jogos, blank=True, related_name="plataformas")

    def __str__(self):
        return f"{self.plataforma}"

class Fotos(models.Model):
    foto = models.ImageField()
