from rest_framework import serializers
from .models import *
from userauth.models import *
from userauth.serializers import *

# Сериализатор модели StateSize (Штатная численность)
class StateSizeSerializer(serializers.ModelSerializer):
      size= serializers.IntegerField(source='statesize')
      class Meta:
            model = StateSize
            fields ='__all__'

# Сериализатор модели FactSize (Фактическая численность)
class FactSizeSerializer(serializers.ModelSerializer):
      size= serializers.IntegerField(source='factsize')
      class Meta:
            model = FactSize
            fields ='__all__'

# Сериализатор модели InspectionDirections (Направление деятельности инспекции)
class InspectionDirectionsSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = InspectionDirections
            fields =['id', 'direction_title', 'icon_name',]


# Сериализаторы структуры инспекции
# class ChiefsDepsSerializer(serializers.ModelSerializer):
#       class Meta:
#             model = DictEmployee
#             fields = [ "id","login","fio","post","room","familyname","email","tel","department"]


# Основной сериализатор структуры инспекции
class StructureSerializer(InfoUserCardSerializer):
    deps = serializers.SerializerMethodField('get_deps',)
    class Meta:
        model = DictEmployee
        fields = '__all__'


    def get_deps(self, obj):
            return  DepsSerializer(obj.deps_curator.filter(deleted=0).all(), many=True).data


class DepsSerializer(serializers.ModelSerializer):
      chief_deps =serializers.SerializerMethodField('get_chief_deps')
      class Meta:
            model = DictDepartment
            fields = '__all__'
      
      def get_chief_deps(self, obj):
            return  InfoUserCardSerializer(obj.id_chief).data


class DepartmentDirectionsSerializer(serializers.ModelSerializer):
      class Meta:
            model = InspectionDirections
            fields = ["id","direction_title"]
            ordering = ['direction_title']




class DepartmentSerializerVac(serializers.ModelSerializer):
      department_directions= DepartmentDirectionsSerializer(many=True, read_only=True)
      class Meta:
            model = DictDepartment
            fields = ['id','name','department_directions']



class VacanciesSerializer(serializers.ModelSerializer):
      department = DepartmentSerializerVac(read_only=True)
      class Meta:
            model = Vacancies
            
            fields = ["id", "department", "name","functional","requirements"]
            