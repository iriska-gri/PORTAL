
from rest_framework import serializers
from .models import *
from commeteresp.models import *



class FileResponsiblitySerializer(serializers.ModelSerializer):

      class Meta:
            model = OrderResponsibilityFiles
            fields = ['file_name', 'id', 'id_order_responsibility']

class CommeetePersonSerializer(serializers.ModelSerializer):


    class Meta:
            model=DictEmployee
            fields=['fio','id', 'login', 'tel', 'room', 'email', 'post', 'department']

class ResponsibilityUsersSerializer(serializers.ModelSerializer):
      fio=serializers.CharField(source='employee.fio')
      id = serializers.IntegerField(source='employee.id')
      login = serializers.CharField(source='employee.login')


      class Meta:
            model=OrderResponsibilityEmployee
            fields=['fio','id', 'login']
            

class OrderResponsibilitySerializer(serializers.ModelSerializer):
    get_resp_files = FileResponsiblitySerializer(many=True, read_only=True)
    users = serializers.SerializerMethodField('respons_users')


    class Meta:
        model = OrderResponsibility
        fields = '__all__'

    def respons_users(self,obj):      
          data = OrderResponsibilityEmployee.objects.filter(id_order_responsibility=obj.id).order_by("employee_id__id_dict_position__order_position","employee_id__familyname")
          return ResponsibilityUsersSerializer(data,many=True).data

class Committee1FilesSerializer(serializers.ModelSerializer):
    """Забирает названия файлов и их актуальность

    """
    class Meta:
        model = Committee1Files
        fields = '__all__'

class Committee1Serializer(serializers.ModelSerializer):
    """ Забирает всю информацию по комиссиям с типом  

    
    """
    typs = serializers.CharField(source='id_dict_committee_type.name')
    files = serializers.SerializerMethodField('get_files')
    
    class Meta:
        model = Committee1
        fields = '__all__'

    def get_files(self, obj):
         data=Committee1Files.objects.filter(id_committee1=obj.id)
         return Committee1FilesSerializer(data, many=True).data

class DictCommitteeOrderAddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictCommitteeOrderAddon
        exclude=['id_committee1']


class Committee2Serializer(serializers.ModelSerializer):
    """ Собирает информацию о комиссиях с файлами"""
    position=serializers.CharField(source='committee_position.name')
    
    name = serializers.CharField(source='id_committee1.name')
    date_start = serializers.DateField(source='id_committee1.date_start')
    date_finish= serializers.DateField(source='id_committee1.date_finish')
    typs = serializers.CharField(source='id_committee1.id_dict_committee_type.name')
    comment = serializers.CharField(source='id_committee1.comment')
    master = serializers.SerializerMethodField('get_master') 
    addons = serializers.SerializerMethodField('get_addons')
    files = serializers.SerializerMethodField('get_files')
    # id_committee1__id_master = serializers.CharField()


    class Meta:
        model = Committee2
        fields = '__all__'

    def get_master(self, obj):
        return  Committee1Serializer(obj.id_committee1.id_master).data
    

    def get_addons(self, obj):
        data=DictCommitteeOrderAddon.objects.filter(id_committee1=obj.id_committee1)
        return DictCommitteeOrderAddonSerializer(data, many=True).data

    def get_files(self, obj):
        data=Committee1Files.objects.filter(id_committee1=obj.id_committee1)
        return Committee1FilesSerializer(data, many=True).data

class CardUserSerializer(serializers.ModelSerializer):
        """Собирает все данные о пользователе
        Используется в представлении getuserAPIView
        В компоненте AboutInspectionPage
        """
        responsibility = serializers.SerializerMethodField('get_responsibility')
        committee = serializers.SerializerMethodField('get_committee')

        class Meta:
            
            model = DictEmployee
            fields = '__all__'
     
        
        def get_responsibility(self, obj):
           
            return [OrderResponsibilitySerializer(x.id_order_responsibility).data for x in obj.user_respons.all()]
          
        

        def get_committee(self, obj):
             return Committee2Serializer(obj.user_committe2.all(), many=True).data



class InfoUserCardSerializer(serializers.ModelSerializer):
    """ Собирает необходимую информацию о пользователе, содержит необходимые
    поля для отрисовки карточки информации о пользователе при клике на фамилию 
    Необходим для компонента infoUserCard"""
    class Meta:            
        model = DictEmployee
        fields = ['department', 'fio', 'post', 'email', 'tel', 'room', 'login', 'familyname', 'name', 'parentname', 'id']
