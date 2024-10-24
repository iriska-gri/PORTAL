from itertools import groupby
from django.db.models import Count
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from userauth.serializers import *
from userauth.models import *
# Create your views here.

class SafetyTypeAPIView(ListAPIView):
    def get(self, request):
        chapters = SafetyType.objects.annotate(Count("mainpage_file")).filter(mainpage_file__count__gt=0)       
        return Response(SafetyTypeSerializer(chapters, many=True).data)

class SafetyAPIView(APIView):
    def get(self, request):
        chapters = self.request.query_params.get('chapter', "fire")
        safety_group = SafetyType.objects.get(path=chapters)    
        return Response(SafetySerializer(safety_group).data)
    
# class SafetyResponsebilityAPIView(APIView):
    
#     def get(self, request):
        
#         fireuser = OrderResponsibility.objects.get(id=54)
#         responsobility_users = OrderResponsibilitySerializer(fireuser)

#         return Response(responsobility_users.data)
    
# class CommitteeFilesAPIView(APIView):

#     def get(self, request):

#         committee_files = Committee1.objects.get(id=106)
#         files = Committee1Serializer(committee_files)

#         return Response(files.data)