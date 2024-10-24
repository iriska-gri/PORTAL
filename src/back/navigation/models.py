from django.db import models
from accounts.models import *
# Create your models here.
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date

class BaseSender(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150, blank=True, db_index=True)
    img = models.ImageField(verbose_name='Картинка', null=True, blank=True, upload_to='senderimage')
    order = models.IntegerField(verbose_name='Порядок сортировки', null=True, blank=True)
    
    class Meta:
 
        verbose_name = "Карусель. Справочник - Статус новости"
        verbose_name_plural = "Карусель. Справочник - Статусы новостей"    

    def __str__(self):
        return str(self.name)

class Links(models.Model): 
    name = models.CharField(db_index=True, max_length=255, verbose_name='Заголовок') 
    link = models.CharField(db_index=True, max_length=255, verbose_name='Ссылка')
    imagecode = models.CharField(db_index=True, max_length=25, verbose_name='Иконка')
    order = models.IntegerField(verbose_name='Порядок сортировки')

    class Meta:
   
        verbose_name = "Ссылка. Внешний ресурс"
        verbose_name_plural = "Ссылки. Внешние ресурсы"

    def __str__(self):
        return str(self.name)

class News(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок') 
    text= RichTextUploadingField(null=True, blank= True, verbose_name='Текст новости')
    cdate =models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Автор')
    link = models.ImageField(upload_to='newsimage/%Y/%m/%d', null=True, default="newsimage/default.jpg", verbose_name='Изображение')
    
    class Meta:

        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def __str__(self):
        return str(self.title)
    
    def names(self):
        return DictEmployee.objects.get(login=self.author)
    
    names.short_description="ФИО"
    

        
class ScoreNews(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Автор')
    score = models.BooleanField(default=None, null=True, verbose_name='Оценка лайк/дизлайк')
    # text= models.TextField(null=True, verbose_name='Сообщение')
    cdate =models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='get_news', verbose_name='Новость')

    class Meta:

        verbose_name = "Новости. Лайк"
        verbose_name_plural = "Новости. Лайки"

    def __str__(self):
        return str(self.author)
    
    def names(self):
        return DictEmployee.objects.get(login=self.author)
    
    names.short_description="ФИО"
    
class Gallery(models.Model):
    img =  models.ImageField(upload_to='newsgallery/%Y/%m/%d', null=True, verbose_name='Изображение')
    news =  models.ForeignKey(News, editable=False, on_delete=models.PROTECT, related_name='get_gallery_news', verbose_name='Новость')
    cdate =models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    

    class Meta:

        verbose_name = "Новости. Изображения"
        verbose_name_plural = "Новости. Изображения"

    def __str__(self):
        return str(self.news)
    

    
class ScoreGallery(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Автор')
    like = models.IntegerField(verbose_name='Лайк', default=0, blank=True)
    cdate =models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, related_name='get_gallery', verbose_name='Новость')

    class Meta:

        verbose_name = "Галерея. Лайк"
        verbose_name_plural = "Галерея. Лайки"

    def __str__(self):
        return str(self.author)

class CommentNews(models.Model):
    text= models.TextField(null=True, verbose_name='Сообщение')
    cdate = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='get_user', editable=False, on_delete=models.PROTECT, verbose_name='Автор')
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='get_comment_news', verbose_name='Новость')

       
    class Meta:
      
        verbose_name = "Новости. Комментарий пользователя"
        verbose_name_plural = "Новости. Комментарии пользователей"

    def __str__(self):
        return str(self.author)
    
    def names(self):
        return DictEmployee.objects.get(login=self.author)
    
    names.short_description="ФИО"

class Carousels(models.Model):
    title=models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок') 
    text= models.TextField(max_length=260, blank=True, null=True, verbose_name='Сообщение')
    cdate =models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Автор новости')
    link = models.ImageField(upload_to='newsimage/%Y/%m/%d', null=True, default="newsimage/default.jpg", verbose_name='Картинка')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    enddate = models.DateTimeField(default=datetime.now().replace(hour=23,minute=0,second=0,microsecond=0) + timedelta(days=7), verbose_name='Дата снятия с публикации')
    sender = models.ForeignKey(BaseSender, on_delete=models.PROTECT, related_name='get_base_sender', verbose_name='Тематика')
    order = models.IntegerField(verbose_name='Порядок сортировки', null=True, blank=True)

    class Meta:

        verbose_name = "Карусель"
        verbose_name_plural = "Карусель"    

    def __str__(self):
        return str(self.title)
    
class BirthdayImage(models.Model):
    img = models.ImageField(verbose_name='Картинка', null=True, blank=True, upload_to='birthdayimage')
    
    class Meta:
  
        verbose_name = "Открытка. Изображение"
        verbose_name_plural = "Открытки. Изображения"    

    def __str__(self):
        return str(self.pk)
    
class BirthdayText(models.Model):
    text= models.TextField(max_length=260, null=True, verbose_name='Текст поздравления')
    
    class Meta:
  
        verbose_name = "Открытка. Текст поздравления"
        verbose_name_plural = "Открытки. Тексты поздравлений"    

    def __str__(self):
        return str(self.pk)  


class Screensaver(models.Model):
    img =  models.ImageField(upload_to='screengallery/%Y/%m/%d', null=True, verbose_name='Изображение')
    cdate =models.DateField(default=date.today().replace(year=1992), null=True, verbose_name='Дата начала периода')
    enddate = models.DateField(default= date.today().replace(year=1992), verbose_name='Дата окончания периода', null=True)
 
    class Meta:

        verbose_name = "Вход. Изображение"
        verbose_name_plural = "Вход. Изображения"

        def __str__(self):
            return str(self.img)
   