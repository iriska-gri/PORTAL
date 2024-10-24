from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class GalleryInline(admin.TabularInline):
    save_on_top = True
    model = Gallery
    fields = ( 'img', 'get_html_photo')
    readonly_fields=('get_html_photo',)
    show_change_link = False
    extra = 1

    def get_html_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50>")
        
    get_html_photo.short_description="Превью изображения"

class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'get_html_photo', 'link', 'names', 'cdate')
    readonly_fields=('get_html_photo',)
    fields=('title', 'text', 'cdate', ('get_html_photo', 'link',))
    list_editable = ('link', 'cdate')
    list_filter = ('cdate',)
    ordering=('-cdate',)
    
    def save_model(self, request, obj, form, change):
        if (request.user.username != 'admin') :
            obj.author = request.user
        else :
            obj.author = User.objects.get(id=15)
        super().save_model(request, obj, form, change)

    def get_html_photo(self, object):
        if object.link:
            return mark_safe(f"<img src='{object.link.url}' width=50>")
        
    get_html_photo.short_description="Превью изображения"

    inlines = [GalleryInline]



class CarouselsAdmin(admin.ModelAdmin):
    list_display=('title', 'get_html_photo', 'link', 'cdate', 'enddate', 'published', 'sender', 'order')
    readonly_fields=('get_html_photo',)
    list_editable=('link','published', 'cdate', 'enddate', 'sender', 'order')
    list_filter=('cdate', 'enddate','published')
    fields=(('title', 'sender'), 'published', 'text', ('cdate', 'enddate'),  ('link','get_html_photo'))

    def save_model(self, request, obj, form, change):

        if (request.user.username != 'admin') :
            obj.author = request.user
        else :
            obj.author = User.objects.get(id=15)
        super().save_model(request, obj, form, change)

    def get_html_photo(self, object):
        if object.link:
            return mark_safe(f"<img src='{object.link.url}' width=50>")
        
    get_html_photo.short_description="Изображение"

class BaseSenderAdmin(admin.ModelAdmin):
    list_display=('name', 'get_html_photo', 'img', 'order')
    list_editable=('img', 'order')
    fields=('name', ('img', 'get_html_photo'))
    readonly_fields=('get_html_photo',)

    def get_html_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50>")
        
    get_html_photo.short_description="Изображение"

class ScoreNewsAdmin(admin.ModelAdmin):
    list_display = ('names', 'news', 'cdate', 'score')
    readonly_fields=('names', 'news', 'cdate', 'score')
    list_filter = ('author', 'cdate', 'score')
    

class CommentNewsAdmin(admin.ModelAdmin):
    list_display = ('names','author', 'news', 'text', 'cdate')
    readonly_fields=('names','author', 'news',  'cdate')
    list_filter = ('author','cdate',)

class LinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    list_display_links = ('link',)

class BirthdayImageAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'img')
    readonly_fields=('get_html_photo',)  
    list_editable=('img',)  
    fields=(('get_html_photo', 'img'),)

    def get_html_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50>")
        
    get_html_photo.short_description="Превью изображения"

class BirthdayTextAdmin(admin.ModelAdmin):
    list_display = ('text',)

class ScreensaverAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'img', 'cdate', 'enddate')
    list_editable=('img', 'cdate', 'enddate')
    fields=(('get_html_photo', 'img'), ('cdate', 'enddate'))
    readonly_fields=('get_html_photo',)    

    def get_html_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50>")
        
    get_html_photo.short_description="Превью изображения"







admin.site.register(Links, LinksAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Carousels, CarouselsAdmin)
admin.site.register(BaseSender, BaseSenderAdmin)
admin.site.register(ScoreNews, ScoreNewsAdmin)
admin.site.register(CommentNews, CommentNewsAdmin)
admin.site.register(BirthdayImage, BirthdayImageAdmin)
admin.site.register(BirthdayText, BirthdayTextAdmin)
admin.site.register(Screensaver, ScreensaverAdmin)
