from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from rest_framework.response import Response
from .serializers import *

class CaorusAPIView(ListAPIView):
    """Карусель с произвольным набором картинок"""
    def get(self, request):
        queryset = Carousels.objects.using('add_base').all().order_by('order')
        return Response(CarouselsSerializer(queryset, many=True).data)