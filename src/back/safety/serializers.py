from rest_framework import serializers
from .models import *
from django.db.models import Count
from commeteresp.serializers import *
from commeteresp.models import *
from userauth.serializers import CommeetePersonSerializer

# class OneFileSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = SafetyFile
#             fields = '__all__'


class SafetyTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = SafetyType
            fields = '__all__'



class Committee1FilesSerializer(serializers.ModelSerializer):
      typeoffile = serializers.SerializerMethodField('typeoffiledef', read_only=True)
      parent = serializers.IntegerField(source = 'id_committee1.id')
      def typeoffiledef(self,obj):
            return 'comm'
      class Meta:
            model = Committee1Files
            fields = ['id','file_name','is_actual', 'typeoffile','parent']






class CometeemembersSerializer(serializers.ModelSerializer):
       position_name = serializers.CharField(source='committee_position.name')
       position_name_short= serializers.CharField(source='committee_position.name_short')
       position_order = serializers.IntegerField(source= 'committee_position.ord')
       fio = serializers.CharField(source='employee.fio')
       emp_id = serializers.IntegerField(source='employee.id')
       login= serializers.CharField(source='employee.login')
      #  DictCommitteePositionSerializer()
      #  employee = CommeetePersonSerializer()
       committee_expert = DictCommitteeExpertSerializer()
       class Meta:
            model = Committee2
            fields = '__all__'


class Commettee1Serializer(serializers.ModelSerializer):
      comtype = serializers.CharField(source="id_dict_committee_type.name")
      master = serializers.CharField(source="id_master.name", allow_null=True)
      com_members = serializers.SerializerMethodField('get_members' , allow_null=True)  
      # CometeemembersSerializer(many=True)
      comitee_files = Committee1FilesSerializer(many=True)
      
      def get_members(data,instance):
            emp = instance.com_members.filter(employee__deleted=0).order_by('committee_position__ord')
            return CometeemembersSerializer(emp,many=True, read_only=True).data



      class Meta:
            model = Committee1
            fields = '__all__'


class OrderResponsibilityFilesSerializer(serializers.ModelSerializer):
      typeoffile = serializers.SerializerMethodField('typeoffiledef', read_only=True)
      parent = serializers.IntegerField(source = 'id_order_responsibility.id')
      def typeoffiledef(self,obj):
            return 'resp'
      class Meta:
            model = Committee1Files
            fields = ['id','file_name','is_actual','typeoffile','parent']

class OrderResponsibilitySerializer(serializers.ModelSerializer):
      employee = serializers.SerializerMethodField('get_respons')  
      get_resp_files = OrderResponsibilityFilesSerializer(many=True)

          
      def get_respons(self, instance):
            employee = [x.employee for x in instance.respons_users.filter(employee__deleted=0)]           
            return CommeetePersonSerializer(employee,many=True, read_only=True).data
      
      class Meta:
            model = OrderResponsibility
            fields = '__all__'
           



class Safety_ResponsibSerializer(serializers.ModelSerializer):
    resp = OrderResponsibilitySerializer() 

    class Meta:
            model = Safety_Responsib
            fields = ['resp']

class Safety_CommiteeSerializer(serializers.ModelSerializer):
    comm = Commettee1Serializer()
 
    class Meta:
            model = Safety_Commitee
            fields = ['comm']
            
class MainpageFileSerializer(serializers.ModelSerializer):
     class Meta:
            model = SafetyFile
            fields = '__all__'

class SafetySerializer(serializers.ModelSerializer):
    mainpage_file = MainpageFileSerializer(many=True, read_only=True)
    type_comm = Safety_CommiteeSerializer(many=True,read_only=True)
    type_resp = Safety_ResponsibSerializer(many=True,read_only=True)
    
    class Meta:
        model = SafetyType
        fields = ['mainpage_file','id','name','type_comm','type_resp']

# class SafetyFileSerializer(serializers.ModelSerializer):
#     # chapter_name = serializers.CharField(source='get_chapter_id_display')
#     # category_name = serializers.CharField(source='get_category_id_display')
#     categories = serializers.SerializerMethodField('get_categories')
#     class Meta:
#         model = SafetyType
#         fields = '__all__'
        
#     def get_categories(self, obj):     

#         files = obj.type_file.all().order_by('category__name')
#         categories = files.values("category","category__name").distinct()
#         for x in files:
#             for y in categories:               
#                 if 'files' not in y.keys():
#                     y['files'] = []
#                 if x.category.id == y['category']:
#                     y['files'].append(OneFileSerializer(x).data)          

#         return categories



    