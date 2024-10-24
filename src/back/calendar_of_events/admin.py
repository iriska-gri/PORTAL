from django.contrib import admin

from .models import *
# Register your models here.

class ExclusionDatesAdmin(admin.ModelAdmin):
    list_display=('exclusiondate',)

admin.site.register(ExclusionDates, ExclusionDatesAdmin)
admin.site.register(Calendar)
admin.site.register(CalendarParticipants)
admin.site.register(Event)
admin.site.register(EventFiles)
admin.site.register(EventParticipant)
