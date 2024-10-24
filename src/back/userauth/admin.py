from django.contrib import admin
from .models import *
from django.db.models import Q
from about_inspection.models import InspectionDirections
# Register your models here.
class DictEmployeeAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    # using = "user_directory"
    list_display=('fio', 'login', 'birthdate')
    search_fields = ('login', 'fio',)
    list_editable=('birthdate',)

class DepartmentDirections(admin.TabularInline):
    model =InspectionDirections
    fields = ( 'direction_title',)
    verbose_name="Направление деятельности отдела"
    verbose_name_plural= "Направления деятельности отдела"
    can_delete = True
    # show_change_link = False
    extra = 0

    
class DictDepartmentAdmin(admin.ModelAdmin):
    readonly_fields=( 'name', 'name_from_ad')
    inlines = [DepartmentDirections]
    def get_queryset(self, request):      
        qs = super().get_queryset(request)
        qs = qs.filter(deleted=0)
        return qs

admin.site.register(DictEmployee,DictEmployeeAdmin)
admin.site.register(DictDepartment, DictDepartmentAdmin )