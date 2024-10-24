
from rest_framework import serializers
from .models import *
from userauth.serializers import *


class LinkSerializer(serializers.ModelSerializer):
      """ Используется в представлении LinkAPIView для внешних ссылок """
      class Meta:
            model = Links
            fields = '__all__'


class ScoreGallerySerializer(serializers.ModelSerializer):
    """Используется для сборки оценкок, для серилизатора GallerySerializer, который нужен для NewsSerializer"""
    user = serializers.CharField(source='author.username')
    class Meta:
        model = ScoreGallery
        fields = ['like', 'user']


class GallerySerializer(serializers.ModelSerializer):
    """Используется для сборки Изображений, для серилизатора NewsSerializer"""
    likes= serializers.SerializerMethodField('get_gallery')
    
    class Meta:
        model = Gallery
        fields = '__all__'

    def get_gallery(self, obj):
        return ScoreGallerySerializer(obj.get_gallery.all(), many=True).data


class ScoreNewsSerializer(serializers.ModelSerializer):
    """Используется для сбора оценок новости, для серилизатора NewsSerializer"""
    user = serializers.CharField(source='author.username')
    class Meta:
        model = ScoreNews
        fields = ['score', 'user']
    

class CommentNewsSerializer(serializers.ModelSerializer):
    """Используется для сборки комментариев, для серилизатора NewsSerializer"""
    
    author = serializers.SerializerMethodField('get_user')

    class Meta:
            model = CommentNews
            fields = '__all__' 

    def get_user(self, obj):
             return InfoUserCardSerializer(DictEmployee.objects.get(login=obj.author.username)).data


class NewsSerializer(serializers.ModelSerializer):
    """ Используется в представлении NewsCrossroadAPIView, собирает информацию по пользователям,
    оставленным новосятим, комментариям, лайкам, изображениям
    """
    show = serializers.SerializerMethodField('get_show')
    showComment = serializers.SerializerMethodField('get_show')
    author = serializers.SerializerMethodField('get_user')
    scores= serializers.SerializerMethodField('get_score')
    comment = serializers.SerializerMethodField('get_comment')
    gallery = serializers.SerializerMethodField('get_gallery')
    
    class Meta:
            model = News
            fields = '__all__'

    def get_show(self,obj):      
          return False
    
    def get_user(self, obj):
             return InfoUserCardSerializer(DictEmployee.objects.get(login=obj.author.username)).data

    def get_score(self, obj):
             return ScoreNewsSerializer(obj.get_news.all(), many=True).data
    
    def get_comment(self, obj):
             return CommentNewsSerializer(obj.get_comment_news.all(), many=True).data
    
    def get_gallery(self, obj):
        #   return 'gal'
            return GallerySerializer(obj.get_gallery_news.all(), many=True).data



class CarouselsSerializer(serializers.ModelSerializer):
    """ Используется в представлении CarouselsAPIView, передает ссылки на картинки для отображения на главной страницы карусели"""
    senders = serializers.CharField(source='sender.img')
    
    class Meta:
            model = Carousels
            fields = ['title', 'text', 'link', 'senders']

  

class ScreensaverSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Screensaver
            fields = '__all__'

class BaseSenderSerializer(serializers.ModelSerializer):
    """ Получить ссылку на картинку для дня рождения. Название 'День рождения'
    автоматически добавляется в таблицу, если его до этого не было """

    class Meta:
            model = BaseSender
            fields = ['img']
