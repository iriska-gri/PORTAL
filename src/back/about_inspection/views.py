from rest_framework.generics import ListAPIView
from django.db.models import Q
from userauth.models import DictEmployee, DictPosition
from datetime import date
from .models import *
from .serializers import *
from rest_framework.response import Response
import json
import requests


class GetStateSize(ListAPIView):
    def get(self, request):
        state_size ={}
        try:
            state_size = StateSizeSerializer(StateSize.objects.latest('date_created')).data
        except Exception as e:
            pass   
     
        return Response(state_size)


class GetFactSize(ListAPIView):
    def get(self, request):
        fact_size = {}
        try:
            fact_size = FactSizeSerializer(FactSize.objects.latest('date_created')).data
        except Exception as e:
            pass    
        return Response(fact_size)


class GetInspectionDirections(ListAPIView):

  queryset = InspectionDirections.objects.filter(department__isnull=True)
  serializer_class = InspectionDirectionsSerializer
  # отключает вывод информации о пагинации(count,previous,next, results)
  paginator = None 

class GetStructure(ListAPIView):
    def get(self, request):
        queryset = DictEmployee.objects.filter(id_dict_position__order_position__lte = 2, deleted=0).order_by('id_dict_position__order_position','familyname')
        return Response(StructureSerializer(queryset, many=True).data)
    

class GetVacancies(ListAPIView):
    def get(self, request):
        queryset = Vacancies.objects.filter(published=True).order_by('department__order_department')
        return Response(VacanciesSerializer(queryset, many=True).data)

class PostResponseVacancies(ListAPIView):
    def post(self, request):
       
        a =  ResponseVacancy.objects.create(**json.loads(request.data['data']), file = request.data['file'] if 'file' in request.data else None)
        print(request.data, 'aaaaaaaaaaaaaa')

        okib = DictDepartment.objects.get(id=22)
        data = {'sendto':[a.vacancy.department.id_chief.lotus, okib.id_chief.lotus], 'subject': f'Отклик на вакансию {a.vacancy.name} от {a.fio}', 'body_text':f'Почта:{a.email} ----- Телефон: {a.tel} ---- Сопроводительное письмо: {a.text}'}
    
        try:
            requests.post('http://10.252.44.13:8005/', data = data, files = [request.data['file']] if 'file' in request.data else [], timeout=2)
        except Exception as e:
            print(e)


        return Response('Ваше резюме отправленно')



