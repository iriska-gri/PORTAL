from django.db import models
from accounts.models import *
# Create your models here.
from django.conf import settings
# from enum import Enum
from ckeditor_uploader.fields import RichTextUploadingField

# class CalendarEventsName(models.Model):
#     """ Глобавльное название календаря"""
#     name=models.CharField(max_length=300, verbose_name='Название Календаря')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Автор Календаря')



# class CalendarEvents(models.Model):
#     """ Основные данные по событиям"""
#     name=models.CharField(max_length=300, verbose_name='Название события') 
#     description = RichTextUploadingField(null=True, blank= True, verbose_name='Описание события')
#     content = RichTextUploadingField(null=True, blank= True, verbose_name='Полное описание события')
#     startdate = models.DateTimeField(null=True, blank= True,  verbose_name='Дата начала события')
#     cdate =models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
#     enddate = models.DateTimeField(null=True, blank= True, verbose_name='Дата снятия с публикации')
#     frequency = models.JSONField(verbose_name='Периодичность', null=True, blank= True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Автор события')
#     place = models.CharField(null=True, blank= True, max_length=500, verbose_name='Место проведения события') 
#     calendarname = models.ForeignKey(CalendarEventsNam, on_delete=models.PROTECT, related_name='get_calendar_events_name', verbose_name='Название для календаря')


#     class Meta:
#         verbose_name = "Календарь событий"
#         verbose_name_plural = "Календарь событий"    

#     def __str__(self):
#         return str(self.name)

# class FilesEvent(models.Model):
#     """ Прикрепленные файлы к событию"""
#     # name = models.CharField(max_length=300, null=True, blank=True, verbose_name='Название файла') 
#     link = models.FileField(upload_to='calendar/%Y/%m/%d')
#     event = models.ForeignKey(CalendarEvents, on_delete=models.PROTECT, null=True, blank= True, related_name='get_calendar_events_files', verbose_name='Событие к которому привязаны файлы')
    
# class ParticipantsEvent(models.Model):
#     """ Участники события """
#     participant = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, verbose_name='Участник события')
#     event = models.ForeignKey(CalendarEvents, on_delete=models.PROTECT, related_name='get_calendar_events', verbose_name='Событие')


# Модели(Таблицы) для хранения календаря
class Calendar(models.Model):
    author = models.ForeignKey(DictEmployee, on_delete=models.PROTECT, verbose_name='Автор календаря')
    cl_name = models.CharField(max_length=300, verbose_name='Название')
    cl_color = models.CharField(max_length=300, verbose_name='Цвет', null=True)
    cl_descr = models.CharField(max_length=300, verbose_name='Описание')


    class Meta:
        verbose_name = "Календарь"
        verbose_name_plural = "Календари"    

    def __str__(self):
        return str(self.cl_name)

class CalendarParticipants(models.Model):
    participant_calendar = models.ForeignKey(DictEmployee,  on_delete=models.PROTECT, verbose_name='Участник')
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='get_participants', verbose_name='Календарь')
    editor = models.BooleanField(default=False, verbose_name='Редактирование')

    class Meta:
        unique_together = ["participant_calendar", "calendar"]
        verbose_name = "Участники календаря"
        verbose_name_plural = "Участники календаря"    

    def __str__(self):
        return str(self.participant_calendar)

class Event(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название', null=True, blank=True)
    # author = models.ForeignKey(DictEmployee, blank=True,null=True,on_delete=models.PROTECT, verbose_name='Автор события')
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='get_calendar_event', verbose_name='Календарь')
    date_start = models.DateTimeField(null=True, blank= True,  verbose_name='Дата начала события')
    date_end = models.DateTimeField(null=True, blank= True, verbose_name='Дата окончания события')
    period = models.JSONField(verbose_name='Периодичность события', null=True, blank= True)
    description = RichTextUploadingField(null=True, blank= True, verbose_name='Описание события')
    allday = models.BooleanField(default=False, verbose_name='Событие на целый день')

    class Meta:
        verbose_name = "Событие календаря"
        verbose_name_plural = "События календаря"    

    def __str__(self):
        return str(self.name)

class EventFiles(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='get_calendar_event_files',blank=True,null=True, verbose_name='Событие')
    file = models.FileField(upload_to='calendar/%Y/%m/%d')

    class Meta:
        verbose_name = "Файлы календаря"
        verbose_name_plural = "Файлы календаря"    

    def __str__(self):
        return str(self.file)

class EventParticipant(models.Model):
    participant = models.ForeignKey(DictEmployee, on_delete=models.PROTECT, related_name='get_user_event', verbose_name='Участник')
    event = models.ForeignKey(Event, blank=True,null=True, on_delete=models.CASCADE, related_name='get_event_participant', verbose_name='Календарь')

    class Meta:
        verbose_name = "Участники события"
        verbose_name_plural = "Участники событий"

    def __str__(self):
        return str(self.participant)


class ExclusionDates(models.Model):
    """ Таблица, которая содержит даты-исключения. То есть, все праздничные дни,
    которые не попадают на выходные и все будни, которые праздничные """
    exclusiondate = models.DateField(null=True, blank= True, verbose_name='Дата-исключение')

    class Meta:
        verbose_name = "Дата-исключение"
        verbose_name_plural = "Даты-исключение"    

    def __str__(self):
        return str(self.exclusiondate)
