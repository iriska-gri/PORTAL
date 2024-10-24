
from rest_framework import serializers
from .models import *
from userauth.serializers import *


class VisitdateSerializer(serializers.ModelSerializer):
      """ Используется в представлении Counter
      выводит дату посещения страницы пользователем
      """
      class Meta:
            model = CountVisitor
            fields = ['visitdate']


class PagesSerializer(serializers.ModelSerializer):
      """Используется для отрисовки страницы статистики в представлении DataForStatisticsAPIView 
      Собирает информацию о посещенных страницах и иинформацию о пользователе из таблицы DictEmployee
      с полями для отрисовки карточки пользователя
      """
      user = serializers.SerializerMethodField('get_user')
      pages = serializers.CharField(source = 'pages.page')
      fullPath = serializers.CharField(source = 'pages.fullPath')
      ico = serializers.CharField(source = 'pages.ico')

      class Meta:
            model = CountVisitor
            fields = ['user', 'pages', 'fullPath', 'ico', 'visitdate', 'count']

      def get_user(self, obj):
            return InfoUserCardSerializer(obj.user.user).data     
