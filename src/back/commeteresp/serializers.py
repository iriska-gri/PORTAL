from rest_framework import serializers
from django.db.models import Count
from .models import *
class DictCommitteePositionSerializer(serializers.ModelSerializer):
     class Meta:
            model = DictCommitteePosition
            fields = '__all__'

DictCommitteeExpert
class DictCommitteeExpertSerializer(serializers.ModelSerializer):
     class Meta:
            model = DictCommitteeExpert
            fields = '__all__'
