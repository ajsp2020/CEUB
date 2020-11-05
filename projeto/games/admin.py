from django.contrib import admin


# Register your models here.
from . models import Jogos, Generos, Plataformas, Desenvolvedores, BlogPost, Post

admin.site.register(Jogos)
admin.site.register(Generos)
admin.site.register(Plataformas)
admin.site.register(Desenvolvedores)
admin.site.register(BlogPost)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','thumbnail_preview')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Post, PostAdmin)


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','thumb')

#     def thumb(self, obj):
#         return  render_to_string('thumb.html',{
#                     'image': obj.image
#                 })

#     thumb.allow_tags = True

