from django.contrib import admin
from .models import *

class GeneralVacationAdmin(admin.ModelAdmin):
    fields = ('login', 'planned_date', 'count_days', 'type_of_vacation', 'start_work_period', 'end_work_period')
    list_display=('get_name', 'login', 'planned_date', 'count_days', 'type_of_vacation', 'start_work_period', 'end_work_period')
    readonly_fields=('get_name',)
    def get_name(self, obj):

        return obj.user.fio()
    
class PlanCalendarAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_work_period', 'end_work_period')
    list_filter = ('start_work_period', 'end_work_period')
    fields = ('name', 'start_work_period', 'end_work_period')

class BasePositionAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    list_editable = ('order', 'name')

# admin.site.register(GeneralVacation, GeneralVacationAdmin),
admin.site.register(PlanCalendar, PlanCalendarAdmin)
admin.site.register(BasePosition, BasePositionAmin)
