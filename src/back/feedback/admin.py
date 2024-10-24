from django.contrib import admin
from .models import *
from django.db.models import Avg

class BaseCriteriaAdmin(admin.ModelAdmin):
    list_display=('name', 'rating')



class RatingStatusInline(admin.TabularInline):
    model = RatingStatus
    fields = ( 'crit', 'rating')
    readonly_fields=( 'crit', 'rating')
    can_delete = False
    show_change_link = False
    extra = 0

class UserCommentAdmin(admin.ModelAdmin):
    fields = ( 'comment', ('get_rat', 'names', 'time_create'))
    list_display=('names', 'comment', 'get_rat', 'utility')
    readonly_fields=('names', 'time_create', 'comment', 'get_rat')
    list_filter=('time_create', 'utility')
    list_editable=('utility', )


    def get_rat(self, obj):
        ratavg = obj.get_rating.aggregate(res=Avg('rating'))
        
        return int(ratavg['res']) if float(ratavg['res']).is_integer() else round(ratavg['res'], 1)
       

    
    get_rat.short_description="Средняя оценка"

    inlines = [RatingStatusInline]



    
# class RatingStatusAdmin(admin.ModelAdmin):
#     # inlines = [RatingStatusInline]
#     fields = ('get_name','get_login', ('crit', 'rating'), 'usercom', 'get_time')
#     list_display=('get_name','get_login', 'crit', 'rating', 'usercom', 'get_time')
    
#     readonly_fields=('get_name','get_login', 'crit', 'rating', 'usercom', 'get_time')
#     list_filter=('crit',)

#     def get_time(self, obj):
#         return obj.usercom.time_create
    
#     def get_name(self, obj):
#         return obj.usercom.user.fio()
    
#     def get_login(self, obj):
#         return obj.usercom.user
    
#     get_time.short_description="Дата создания"
#     get_name.short_description="ФИО"
#     get_login.short_description="Логин"

admin.site.site_header = "Админ-панель сайта Портал"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"

admin.site.register(BaseCriteria, BaseCriteriaAdmin)
admin.site.register(UserComment, UserCommentAdmin)
# admin.site.register(RatingStatus, RatingStatusAdmin)

# Register your models here.
