from rest_framework.response import Response
import datetime
from .serializers import *
from .models import *

from rest_framework.views import APIView

 
class FeedbackAPIView(APIView):

    def get(self, request):
        """Оценка сайта. Собираем информацию о критериях оценки, поставленный рейтинг и коментарий"""
       
        nowrating = RatingStatus.objects.filter(usercom__user_id=self.request.user.id,
                                                usercom__time_create__contains=datetime.date.today()
                                                ).order_by("crit_id")
        nowcomment = UserComment.objects.filter(user_id=self.request.user.id,
                                                time_create__contains=datetime.date.today()
                                                )
        basecrit = BaseCriteria.objects.all()

        # Сериализуем извлечённый набор записей
        serializer_for_basecrit = BaseCriteriaAllSerializer(
            instance=basecrit, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )

        serializer_for_nowcomment = FeedbackUserCommentSerializer(
            instance=nowcomment, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )

        serializer_for_nowrating = RatingStatusSerializer(
            instance=nowrating, # Передаём набор записей , "rat":serializer_for_queryset2.data
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        
        return Response({"basecrit": serializer_for_basecrit.data,
                         "nowrating": serializer_for_nowrating.data,
                         "nowcomment": serializer_for_nowcomment.data[0] if len(nowcomment)>0 else None
                        })
    
    def post(self, request):
        """Оценка сайта. И добавление или обновление комементария или оценки сайта
        Параметры
        nowrating - массив объектов nowrating  {id: 34, rating: 3, crit: 1, usercom: 13}
        объект nowcomment {id: 13, time_create: '2024-03-18T13:38:41.421851+03:00', comment: '', utility: true, user: 22}
        """
        comment, created = UserComment.objects.update_or_create(id = request.data['nowcomment']['id'],
                                                                user_id = self.request.user.id,
                                                                defaults = {'comment':request.data['nowcomment']['comment'],
                                                                          'time_create':datetime.datetime.now()
                                                                          })
        for x in request.data['nowrating']:
           RatingStatus.objects.update_or_create(id=x['id'],
                                                 defaults={'rating':x['rating'],
                                                           'crit_id':x['crit'],
                                                           'usercom_id':comment.id
                                                           })
        return Response({})

    








