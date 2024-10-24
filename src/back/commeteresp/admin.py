from django.contrib import admin
from .models import *
from userauth.models import DictEmployee
# Register your models here.


# admin.site.register(Committee1)


# class DictEmployeeAdmin(admin.ModelAdmin):
class IlineComitteeFiles(admin.StackedInline):
    
    fields = ('file_name','is_actual',)
    model = Committee1Files
    extra = 0

class InlineComiteePeople(admin.StackedInline):
    model = Committee2
    extra = 0

class Committee1Admin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ( 'num_start', 'name',)
    search_fields = ('num_start', 'name',)
    inlines = [IlineComitteeFiles, InlineComiteePeople]

class InlineRespFiles(admin.StackedInline):
    model = OrderResponsibilityFiles
    extra = 0


class InlineRespEmp(admin.StackedInline):
    model = OrderResponsibilityEmployee
    extra=0
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'employee':
            kwargs['queryset'] = DictEmployee.objects.filter(deleted=0)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class OrderResponsibilityAdmin(admin.ModelAdmin):
    # model= OrderResponsibility
    list_display = ( 'number', 'name')
    search_fields = ('number', 'name',)
    inlines=[InlineRespFiles,InlineRespEmp]





admin.site.register(Committee1, Committee1Admin)
admin.site.register(OrderResponsibility, OrderResponsibilityAdmin)
