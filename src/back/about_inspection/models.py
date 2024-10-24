from django.db import models
from userauth.models import DictDepartment
from ckeditor_uploader.fields import RichTextUploadingField

# Модель Штатная численность
class StateSize(models.Model):
    statesize = models.IntegerField( verbose_name="Штатная численность")
    date_created = models.DateField(verbose_name="Дата создания")
    class Meta:
        verbose_name = "Штатная численность"
        verbose_name_plural = "Штатная численность"
    def __str__(self):
        return str(self.statesize)    
    
#Модель Фактическая численность
class FactSize(models.Model):
    factsize = models.IntegerField( verbose_name="Фактическая численность")
    date_created = models.DateField(verbose_name="Дата создания")
    class Meta:
        verbose_name = "Фактическая численность"
        verbose_name_plural = "Фактическая численность"
    def __str__(self):
        return str(self.factsize)    


# Модель Направление деятельности инспекции
class InspectionDirections(models.Model):
    direction_title = models.CharField(max_length=255, verbose_name="Направление деятельности")
    icon_name = models.CharField(max_length=100, verbose_name="Название иконки", default="mdi-sign-direction" ,blank=True)
    department = models.ForeignKey (DictDepartment,on_delete=models.PROTECT, null=True, blank=True,  verbose_name='Отдел', related_name='department_directions')
   
    class Meta:
        verbose_name = "Направление деятельности "
        verbose_name_plural = "Направления деятельности"
    def __str__(self):
        return self.direction_title
    
class Vacancies(models.Model):
    name=models.TextField(verbose_name="Наименование")
    department = models.ForeignKey (DictDepartment,on_delete=models.PROTECT, null=True, blank=True,  verbose_name='Отдел')
    functional = RichTextUploadingField(null=True, blank= True, verbose_name='Функционал и должностные обязанности')
    requirements = RichTextUploadingField(null=True, blank= True, verbose_name='Базовые требования к соискателю')
    published = models.BooleanField(default = False, verbose_name="Опубликована")

    class Meta:
        verbose_name = "Вакансия "
        verbose_name_plural = "Вакансии"
    def __str__(self):
        return self.name
    
# Отклик на вакансию
class ResponseVacancy(models.Model):
    fio = models.CharField(max_length=300, verbose_name='ФИО') 
    cdate = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField(null=True, verbose_name='Сообщение')
    email = models.CharField(null=True,max_length=300, verbose_name='Почта') 
    tel = models.CharField(null=True,max_length=300, verbose_name='Номер телефона') 
    file = models.FileField(null=True, upload_to='response/%Y/%m/%d', verbose_name='Файл резюме')
    vacancy = models.ForeignKey(Vacancies, on_delete=models.PROTECT, related_name='get_vacancies', verbose_name='Вакансия')

    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансию"
    def __str__(self):
        return self.fio