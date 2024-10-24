
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
import jwt
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
# from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ValidationError
# from orgmanagment.models import *
from datetime import datetime, timedelta
import requests
from django.contrib.auth import authenticate
import json
from django.forms.models import model_to_dict
from userauth.models import DictEmployee

# all_fk: dict = {
#     "otdel": Otdel,
#     "department": Department,
#     "organization":Organization,
#     "position": Position,
#     "rank": Rank
# }    
    
# class Position(models.Model):
#     name= models.CharField(verbose_name='Название', max_length=150, blank=True)
#     class Meta:
#             verbose_name = "Должность"
#             verbose_name_plural = "Должности"
#     def __str__(self):
#         return str(self.name)

class UserManager(BaseUserManager):

    def create_superuser(self, username,  password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username,  password)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()

        return user
        


class User(AbstractBaseUser, PermissionsMixin): 
    user = models.ForeignKey(DictEmployee, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Сотрудник')
    password = models.CharField(max_length=128, null=True,blank=True,verbose_name='Пароль')
    username = models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Логин') 
    # username2 = models.CharField(db_index=True, null=True, max_length=255, unique=True) 
    is_active = models.BooleanField(default=True, verbose_name='Активность')  
    is_staff = models.BooleanField(default=False, verbose_name='Доступ в Админку')    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # last_login =  models.DateTimeField(auto_now=True, null=True)
    # external=models.ForeignKey(DictEmployee,db_constraint=False, null=True, on_delete=models.PROTECT)
    objects = UserManager()

    

   

    class Meta: 
    
        verbose_name = "Зарегистрированный участник"
        verbose_name_plural = "Зарегистрированные участники"

    USERNAME_FIELD = 'username'
    
    # REQUIRED_FIELDS = ['username']
    def __str__(self):
        return str(self.username)
   
    def fio(self):

        return self.user.login

    
    def names(self):
        return DictEmployee.objects.get(login=self.username)
    
    names.short_description="ФИО"