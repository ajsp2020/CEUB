from django.db import models

# Create your models here.

class Filmes(models.Model):
    name = models.CharField(max_length=64)
    duration = models.IntegerField()
    gen = models.CharField(max_length=64)
    diretor = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}, {self.duration} min, {self.gen}"
