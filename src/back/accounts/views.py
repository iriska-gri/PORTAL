from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from userauth.models import *
from navigation.models import *
from navigation.serializers import *
from userauth.serializers import *
from .models import *
from .serializers import *


class getuserAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        """
        Параметр: userlogin
        Пример: GET /api/accounts/getuser/?userlogin=9966-00-107
        Результат: Выдает все данные о пользователе
        Если дать дополнительный параметр fullinfo = True, то будет выдаваться информация с комиссиями и ответсвенностью
        """
        resp = None
        fullinfo = request.query_params.get('fullinfo')
        queryset = DictEmployee.objects.get(login=request.query_params.get('userlogin'))
        if(fullinfo is None or fullinfo == False ):
            resp = InfoUserCardSerializer(queryset).data

        else:
            resp = CardUserSerializer(queryset).data
        
        return Response(resp)
    

