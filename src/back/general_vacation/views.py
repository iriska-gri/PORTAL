from datetime import datetime
from .excel import roundExcel, loadExcel
import os
from django.forms import model_to_dict
from openpyxl import load_workbook
import openpyxl
from rest_framework.response import Response
from datetime import date
from .serializers import *
from .models import *
import pandas as pd
from rest_framework.views import APIView
from userauth.models import *
from django.shortcuts import render
from pandas.io.excel import ExcelWriter
import openpyxl as oxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Side, Border, PatternFill
from openpyxl.worksheet.formula import ArrayFormula
from pandas.api.types import CategoricalDtype
import urllib.request
from django.db.models import Count

class GeneralVacationAPIView(APIView):
    def get(self, request):
        """В работе. Необходимо для учета отпуска сотрудников"""
        general = GeneralVacation.objects.all()
        plan = PlanCalendar.objects.all()

                # Сериализуем извлечённый набор записей
        serializer_for_basecrit = GeneralVacationSerializer(
            instance=general, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )

        serializer_for_plan = PlanCalendarSerializer(
            instance=plan, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return Response({"Отпуск": serializer_for_basecrit.data, "План-график": serializer_for_plan.data})
    
class DailyRoundUpAPIView(APIView):
   
    def get(self, request):
        """Принимает файл и в параметр excel передается имя функции, которую нужно использовать. excround - На формирование файла"""
        user = DictEmployee.objects.filter(deleted=0).values('login', 'department', 'familyname', 'name', 'parentname').order_by('id_dict_department__order_department')
   
      
        re = roundExcel(user)

        file_path = getattr(re, request.GET.get("excel"))()
        # if request.GET.get("excel") == 'round':
        #     file_path = re.excround()
        # if request.GET.get("excel") == 'vacation':
        #     file_path = re.excelvacation()
       
        
    



        
        return Response({'path':file_path})

        

    def post(self, request):
        """Принимает файл и в параметр excel передается имя функции, которую нужно использовать. roundfilse - на загрузку в бд"""
        print(request.data, 'request.data')
        user = DictEmployee.objects.filter(deleted=0).values('login', 'id', 'fio')
        re = loadExcel(user, request.data['dailyfiles'])
        pos=''
        mess = 'Файл не найден'
        try:
            getattr(re, request.GET.get("excel"))()
            mess = 'Файл загружен'
        except Exception as e:
     
            pass
        
                 
     


        
        return Response({"mess": mess, "pos": pos}) 


class DailyloadAPIView(APIView):
    """Читает загружаемый файл эксель, записывает данные в бд - информация  о пользоватаеле и его местонахождение. Сортировка по департаменту, затемпо местонахождению, потом по фамилии
    может принимать параметр id наименования местонахождения
    """
    def get(self, request):
        try:
            user = DictEmployee.objects.filter(deleted=0).values('login', 'department', 'fio', 'post', 'email', 'tel', 'room').order_by('id_dict_department__order_department', 'id_dict_position__order_position', 'fio')
          
            dailyr = DailyRoundUp.objects.filter(todaysDate=date.today()).values_list('user', 'position__name', 'position')
            df_user = pd.DataFrame.from_records(user)
            df_daily = pd.DataFrame.from_records(dailyr)
            df_daily.columns = ["login",  "pos", "idpos"]
           
            df = pd.merge(df_user, df_daily, left_on= 'login', right_on="login")
            
            result={}

            

            if request.GET.__contains__('id'):
                df=df.loc[df['idpos']==int(request.GET.get("id"))]
                pos=df['pos'].unique()[0]
                if request.GET.__contains__('searchname'):

                    df = df.loc[df["fio"].str.contains(request.GET.get("searchname"))] 
            
            
                
                for index, row in df.iterrows ():
                    if row['department'] in result.keys():
                        result[row['department']].append({'login':row['login'],
                                                          'fio':row['fio'],
                                                          'post':row['post'],
                                                          'pos':row['pos'],
                                                          'email':row['email'],
                                                          'department':row['department'],
                                                          'tel':row['tel'],
                                                          'room':row['room']

                                                          })
                    else:
                        result[row['department']]=[{'login':row['login'],
                                                    'fio':row['fio'],
                                                    'post':row['post'],
                                                    'pos':row['pos'],
                                                    'email':row['email'],
                                                    'department':row['department'],
                                                    'tel':row['tel'],
                                                    'room':row['room']
                                                    }]
                
                daily = result

                
            

            else:
                pos=''
                daily = DailyRoundUp.objects.values('position__name', 'position').filter(todaysDate=date.today()).annotate(Count('user')).order_by('position__order')
        except Exception as e:
            pos=''
            daily=""
        return Response({'daily':daily, 'position':pos})
    

