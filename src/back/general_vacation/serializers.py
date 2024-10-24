from rest_framework import serializers
from .models import *

class GeneralVacationSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = GeneralVacation
            fields ='__all__'

class PlanCalendarSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = PlanCalendar
            fields ='__all__'

class DailyRoundUpSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = DailyRoundUp
            fields ='__all__'
            