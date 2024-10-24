
from rest_framework import serializers
from .models import *



class CarouselsSerializer(serializers.ModelSerializer):
      class Meta:
           
            model = Carousels
            fields = '__all__'
