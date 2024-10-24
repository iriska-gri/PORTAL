from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
import json
from django.db.models.functions import TruncYear
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
import os


class ExclusionDatesAPIView(APIView):
    def get(self, request):
        year = self.request.query_params.get('year', datetime.now().year)
        exclude = ExclusionDates.objects.filter(exclusiondate__year=year)
        months = {}
        for i in range(1,12):
            months[i] = exclude.filter(exclusiondate__month=i).values_list("exclusiondate", flat=True)
        return Response({year:months})


class MyCalendars(APIView):
    
    def get(self, request):        
        calendars = Calendar.objects.filter(Q(get_participants__participant_calendar__id=request.user.user.id) | Q(author__id=request.user.user.id)).distinct()
        return Response(CalendarsSerializer(calendars,many=True).data)
    
    @swagger_auto_schema(request_body=MyCalendarPostParameters)
    def post(self,request):
        '''
        Создание/редактирование календаря
        если нет id = пойдет создавать календарь. В противном случае - на обновление


        '''  

        try:   
           
            ob=MyCalendarPostParameters(data=request.data)  
            
            if ob.is_valid():
                ob = ob.data  
                participant = ob['participant'] if 'participant' in ob else False
                
                del ob['participant']        
                if 'id' in ob:               
                    newcal,created = Calendar.objects.update_or_create(id=ob['id'],defaults=ob)
                    
                else:            
                    newcal=Calendar.objects.create(**ob, author=DictEmployee(id=request.user.user.id))
              
                if participant != False:
                    ptspnt = []
                   
                    for x in participant:
                        x['participant_calendar']=DictEmployee(id=x['participant_calendar'])
 
                        newpart, created = CalendarParticipants.objects.update_or_create(calendar=newcal, participant_calendar=x['participant_calendar'],
                                                                                defaults=x)
                       
                        ptspnt.append(x['participant_calendar'])
                    print(ptspnt)
                    CalendarParticipants.objects.exclude(participant_calendar__in=ptspnt).filter(calendar=newcal).delete()  
            else:
                return Response({"mess":"Ошибка валидации полей"})
        except Exception as e:
            print(e)
            return Response({"mess":"Ошибка операции"})

        return Response({"mess": f"Календарь успешно {'обновлен' if 'id' in ob else 'создан'}"})



    @swagger_auto_schema(query_serializer=DeleteCalendarSerializer)
    def delete(self,request):
        try:
            Calendar.objects.get(id=request.query_params.get("delid")).delete()
        except Exception as e:
            print(e)
            return Response({'mess':'Удаление не удалось'})
        return Response({"mess": "Календарь удален"})
        

class GetEmployees(APIView):
    def get(self, request):
        
        queryset = DictDepartment.objects.filter(deleted=0,id__gt=0)
       
        return Response(EmployeeSerializer(queryset, many=True).data)



class MyEvents(APIView):
    parser_classes = [MultiPartParser]
    @swagger_auto_schema(query_serializer=IdonlyRequieredSerializer)
    def get(self, request):
        allcalendars = Calendar.objects.filter(Q(get_participants__participant_calendar__id=request.user.user.id ,get_participants__editor=1) | Q(author__id=request.user.user.id)).distinct()
        resp = {'mycalendars':CalendarsSerializerForEventEdit(allcalendars, many=True).data }
        if request.query_params.get("id") is not None:
            event = Event.objects.get(id = request.query_params.get("id"))
            resp['event']=EventSerializerIdRequest(event).data    
        return Response(resp)
    
    
    
    @swagger_auto_schema(
            request_body=CreateUpdateEventSerializer,   
            manual_parameters=[             
              
                openapi.Parameter('event', openapi.IN_FORM, type=openapi.TYPE_STRING, description='JSON', required=True,
                                  ),
                openapi.Parameter('files', openapi.IN_FORM, type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_FILE), description='Документы'),])
    
    # @parser_classes([MultiPartParser])
    def post(self, request):
      
        '''
        К сожалению, у этого сваггера есть ограничения на несколько файлов, поэтому тут схемы для них не будет
        Но мы будем отправлять ровно также
        event = JSON строка  
       "id": 1,  //не обязательно
        "name": "2d1",
        "date_start": "2024-05-28T16:10:41+03:00",
        "date_end": "2024-06-06T16:10:43+03:00",
        "period": JSON.stringify({"lll":'dkdjk'}),
        "description": "ыуаыаы",
        "calendar": 8,
        'participant':[125,1],
        'files':[объекты файлов, которые не будут удалены] 

        'allday':boolean  -добавлено 19072024
        '''
#         event = json.dumps(    {
#         "id": 1,  
#         "name": "2d1",
#         "date_start": "2024-05-28T16:10:41+03:00",
#         "date_end": "2024-06-06T16:10:43+03:00",
#         "period": json.dumps({"lll":'dkdjk'}),
#         "description": "<p>ыуаыаы</p>",
#         "calendar": 8,
#         'participant':[1,125],
#         'files':[] 
#   })
        created=True
      
        try:
            event = json.loads(request.data['event'])
            # event = json.loads(event)
        
            filesadd = request.FILES.getlist('files') 
            
            # participant=request.POST['participant']
            participant= event['participant']
         

           
            event['calendar']=Calendar(id=event['calendar'])
       
            files = [x['id'] for x in event['files']]

            del event['files']
            del event['participant']
      
        
            evnt=None
            if 'id' in event:  
                evnt,created=Event.objects.update_or_create(id=event['id'], defaults = event)

            else:
                evnt=Event.objects.create(**event)    

            
            for x in participant:
                EventParticipant.objects.update_or_create(event=evnt,participant=DictEmployee(id=x))
            
            EventParticipant.objects.filter(event=evnt).exclude(participant__id__in=participant).delete()


            delfiles = EventFiles.objects.filter(event=evnt).exclude(id__in=files)

            for x in delfiles:
                try:
                    os.remove(os.path.join(settings.MEDIA_ROOT, x.file.name))
                except Exception:
                    pass
            delfiles.delete()

            for x in filesadd:
                EventFiles.objects.create(event=evnt,file=x)


            return Response({'mess':f'Событие {"создано" if created==True else "обновлено"}'})
        except Exception:
            return Response({'mess':f'Произошла ошибка'})
    
    @swagger_auto_schema(query_serializer=DeleteCalendarSerializer)
    def delete(self,request):
        try:
            Event.objects.get(id=request.query_params.get("delid")).delete()
        except Exception as e:
            print(e)
            return Response({'mess':'Удаление не удалось'})
        return Response({"mess": "Событие удалено "})