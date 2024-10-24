from django.contrib import admin

from .models import *
# Register your models here.
class MainpageInline(admin.StackedInline):
    model = SafetyFile
    extra = 0
    
class ResponsFilesInline(admin.StackedInline):
    model = Safety_Responsib
   
    # fields = ('resp',)
    # ordering = ("resp",)
    # readonly_fields=( 'crit', 'rating')
    # can_delete = False
    # show_change_link = False
    extra = 0
class Safety_CommiteeInline(admin.StackedInline):
    model = Safety_Commitee
    fields = ('comm',)
    ordering = ("comm",)
    extra = 0

# class SafetyFileAdmin(admin.ModelAdmin):
    
#     list_display = ('name', 'chapter', 'category', 'sign_date', 'formainpage')
#     list_editable = ('sign_date', 'category', 'formainpage')
#     list_filter = ('name', 'sign_date', 'category',)
#     fields = ('name', 'url', 'chapter', 'category', 'sign_date', 'formainpage')
    
class SafetyTypeAdmin(admin.ModelAdmin):
     inlines = [MainpageInline, ResponsFilesInline, Safety_CommiteeInline]



admin.site.register(SafetyType,SafetyTypeAdmin)
# admin.site.register(SafetyDocumentCategory)
# admin.site.register(SafetyFile, SafetyFileAdmin)
