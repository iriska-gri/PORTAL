from rest_framework import serializers
from .models import *
from about_inspection.models import *
from  userauth.serializers import *
class IdonlyRequieredSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)

class CalendarParticipantsSerializer(serializers.ModelSerializer):
    """ Сериализатор участников календаря """
    
    class Meta:
        model = CalendarParticipants
        exclude = ['calendar']




class EventParticipantSerializer(serializers.ModelSerializer):
    """ Сериализатор участников календаря """
    
    class Meta:
        model = CalendarParticipants
        exclude = ['event']

class EventParticipantSerializerIDonly(serializers.RelatedField):
    def to_representation(self, value):        
        return value.participant.id
    # pass

class CalendarEventSerializer(serializers.ModelSerializer):
    """ Сериализатор событий календаря """
    # participant = EventParticipantSerializerIDonly(many=True, read_only=True, source='get_event_participant')
    class Meta:
        model = Event
        fields = '__all__'



class CalendarsSerializer(serializers.ModelSerializer):
    """ Сериализатор календарей """
    
    events = CalendarEventSerializer(source="get_calendar_event", many=True, allow_null=True)
    participant = CalendarParticipantsSerializer(source="get_participants", many= True, read_only=True)

 
    # def is_editor(self, obj):
    #     r = self.context.get("request")        
    #     return obj.get_user.filter(participant_calendar=r.user.user.id).last().editor

    class Meta:
        model = Calendar
        fields = '__all__'







class CalendarParticipantsSerializerFullInfo(serializers.ModelSerializer):
    def to_representation(self, value):        
        return UserSerializerBase(value.participant_calendar).data
    class Meta:
        model = CalendarParticipants
        exclude = ['calendar']


class CalendarsSerializerForEventEdit(serializers.ModelSerializer):
    """ Сериализатор календарей для окна редактирования событий"""  
    
    participant = CalendarParticipantsSerializerFullInfo(source="get_participants", many= True, read_only=True)


    class Meta:
        model = Calendar
        fields = '__all__'

class EventFilesSerializer(serializers.ModelSerializer):
    """ Сериализатор файлов календаря """

    class Meta:
        model = EventFiles
        fields = '__all__'


class EventSerializerIdRequest(serializers.ModelSerializer):
    participant = EventParticipantSerializerIDonly(source="get_event_participant", many= True, read_only=True)
    files = EventFilesSerializer(many=True, source='get_calendar_event_files')
    class Meta:
        model = Event
        fields = '__all__'




class TableEventParticipantSerializer(serializers.ModelSerializer):
    """ Сериализатор участников календаря """

    class Meta:
        model = EventParticipant
        fields = '__all__'

# Запрос сотрудников

class EmployeeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')
    selected=serializers.BooleanField(default=False)
    editor=serializers.BooleanField(default=False)
    employees = serializers.SerializerMethodField('get_deps')
    class Meta:
        model = DictDepartment
        fields = ["title","id","employees",'selected', 'editor']
        
    def get_deps(self,obj):
       
        return UsersSerializer(obj.dep_user.filter(deleted=0), many=True).data
    
    # 
class UserSerializerBase(serializers.ModelSerializer):
    title = serializers.CharField(source='fio')
    class Meta:
        model = DictEmployee
        fields = ['title', "id" ]

class UsersSerializer(UserSerializerBase):
    editor=serializers.BooleanField(default=False)
    selected=serializers.BooleanField(default=False)
    class Meta:
        model = DictEmployee
        fields = ['title', "id", 'id_dict_department','selected','editor' ]


class DeleteCalendarSerializer(serializers.Serializer):
    delid = serializers.IntegerField()


class MyCalendarPostParametersParticipants(serializers.ModelSerializer):

 class Meta:
        model = CalendarParticipants
        exclude = ['calendar','id']





class MyCalendarPostParameters(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    # author = serializers.IntegerField(required=False)
    participant = MyCalendarPostParametersParticipants(source="get_participants", many=True, required=False)
   

    class Meta:
        model = Calendar
        exclude =['author']

    
class CreateUpdateEventSerializer(serializers.Serializer):
    event = serializers.JSONField()
    # participant= serializers.ListSerializer(child=serializers.IntegerField(), required=False)

    # class Meta:
    #     model = Event
    #     fields = '__all__'