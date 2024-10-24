from django.contrib import admin
from .models import *
from userauth.models import DictDepartment
from django.db.models import Q

class InspectionDirectionsAdmin(admin.ModelAdmin):
    list_display=('direction_title',)
    fields=('direction_title','icon_name',)
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['direction_title'].label += " инспекции"
        return form

    def get_queryset(self, request):      
        qs = super().get_queryset(request)
        qs = qs.filter(department__isnull=True)
        return qs

class VacanciesAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['department'].queryset = DictDepartment.objects.filter(~Q(name="Все сотрудники"),deleted=0)
        return form
    
class ResponseVacancyAdmin(admin.ModelAdmin):
    list_display = ('fio', 'cdate', 'email', 'tel', 'vacancy')
    readonly_fields = ('fio', 'cdate', 'text', 'email', 'tel', 'file', 'vacancy')
    list_filter = ('cdate', 'vacancy__department')

admin.site.register(Vacancies,VacanciesAdmin)
admin.site.register(StateSize)
admin.site.register(FactSize)
admin.site.register(InspectionDirections, InspectionDirectionsAdmin)
admin.site.register(ResponseVacancy, ResponseVacancyAdmin)
