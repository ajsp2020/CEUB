from django.db import models

from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.


class Desenvolvedores(models.Model):
    desenvolvedor = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.desenvolvedor}"


class Jogos(models.Model):
    
    nome = models.CharField(max_length=64)
    dataLancamento = models.IntegerField()
    projetista = models.CharField(max_length=64,blank=True)
    desenvolvedor = models.ForeignKey(Desenvolvedores, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.nome}"

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


class BlogPost(models.Model):
    # id - Django automatically creates an auto-incrementing primary key for every model!
 
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=True)
    slug = models.CharField(max_length=240, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    nome = models.ForeignKey(Jogos, on_delete=models.CASCADE, null=True, blank=True)



class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='static/games/imagens/%Y/%m/%d/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""



