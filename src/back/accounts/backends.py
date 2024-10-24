import jwt
import requests
import json
from django.conf import settings
from portal.settings import myDEBUG
from django.forms.models import model_to_dict
from rest_framework import authentication, exceptions
from datetime import datetime
from .models import User
from userauth.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
User = get_user_model()


# class Authexception(Exception):
#     def __init__(self, *args):
#         self.message = args[0] if args else "None"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        try:
            token = super().get_token(user.userinfo)

            # TODO В зависимости от базы Алексея, добавить поля или нет - надо подумать
            
            
            token['user']=model_to_dict(user.userinfo)
            token['user']['is_active']=user.is_active
            token['user']['is_staff']=user.is_staff
            token['user']['is_superuser']=user.is_superuser
            token['user']['is_idEmployee']=user.user_id
            # !ТУТ СДЕЛАТь ФОТО НАВЕРНОЕ
            # token['user']['last_login']= user.last_login
            # print(token)
            return token
        except Exception as e:
            print("ERRRORRRRRRRR")
            print (e)
    
    
    
from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
from django.utils import timezone

class CustomAuth(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        status_code=0
        
        # !ТУт стучим в AD, потом к Алексею
        if myDEBUG!=True: 

            resp= requests.post('http://10.252.44.13:8005/getAD', json.dumps({'user': username, 'password':password, 'usercheck': username}))
            
            # if True:
            status_code=resp.status_code
        else:
            
            status_code=200
            # status_code=403
        

        if status_code==200:
            # try:

            user = DictEmployee.objects.get(login=username)
            
            if user.deleted!=1:
                homeuser, created = User.objects.get_or_create(username=username)
                if created:
                    homeuser.set_unusable_password()

                homeuser.last_login= timezone.now()
                homeuser.user=user
                user.is_active=homeuser.is_active
                user.is_staff=homeuser.is_staff
                user.is_idEmployee=homeuser.user_id
                user.last_login=homeuser.last_login.strftime('%Y-%d-%m %H:%M:%S')                    
                homeuser.save()
                if user.birthdate is not None:
                    homeuser.birthdate = user.birthdate.strftime('%Y-%d-%m %H:%M:%S') 
                else:
                    homeuser.birthdate = None
                user.birthdate=homeuser.birthdate
                homeuser.last_login=user.last_login
                user.id=homeuser.id 
                homeuser.userinfo = user   
           
                return homeuser
                
      