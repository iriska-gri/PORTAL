from rest_framework import serializers
from .models import *
from userauth.serializers import *

class BaseCriteriaAllSerializer(serializers.ModelSerializer):
      """ Забирает все поля из модели по хранению названия критерия оценки,
      используемой иконки, рейтинга по умолчанию, и цвет для иконки
      Используется в представлении FeedbackAPIView в компоненте cardLike
      """ 
      class Meta:
            model = BaseCriteria
            fields = '__all__'


class RatingStatusSerializer(serializers.ModelSerializer):
      """ Забирает все поля из модели по хранению критерия оценки,
      какую поставили по критерию, и к какому коментарию оно относится 
      Используется в представлении FeedbackAPIView в компоненте cardLike
      """
      class Meta:
            model = RatingStatus
            fields ='__all__'
            

class FeedbackUserCommentSerializer(serializers.ModelSerializer):
      """ Забирает все поля из модели, без расшифровки пользователя
      Используется в представлении FeedbackAPIView в компоненте cardLike
      """          
      class Meta:
            model = UserComment
            fields = '__all__'

            
class UserCommentSerializer(serializers.ModelSerializer):
      """Используется в представлении DataForStatisticsAPIView, для сбора информации
      feed - берет все поля из модели с UserComment, и добавляет информацию об авторе
      """
      author = serializers.SerializerMethodField('get_user')          
      class Meta:
            model = UserComment
            fields = '__all__'

      def get_user(self, obj):
            return InfoUserCardSerializer(obj.user.user).data  