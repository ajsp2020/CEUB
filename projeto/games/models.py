from django.db import models


from django.utils.html import mark_safe
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

class Imagens(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""







class BlogPost(models.Model):
    # id - Django automatically creates an auto-incrementing primary key for every model!
 
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.CharField(max_length=240, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    nome = models.ForeignKey(Jogos, on_delete=models.CASCADE, null=True)