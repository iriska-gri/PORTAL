from django.db import models  

# Create your models here.

# class SafetyDocumentCategory(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return str(self.name)

class SafetyType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название подраздела')
    path = models.CharField(max_length=255, null=True, verbose_name='Путь')
    # path1 = models.CharField(max_length=255, null=True, verbose_name='Путь')
    class Meta:

        verbose_name = 'Подраздел'
        verbose_name_plural = 'Подразделы'

    def __str__(self):
        return str(self.name)

class Safety_Responsib(models.Model):
    type =  models.ForeignKey('SafetyType', models.DO_NOTHING, null=True, verbose_name='Раздел', related_name="type_resp")
    resp = models.ForeignKey('commeteresp.OrderResponsibility', models.DO_NOTHING, null=True, verbose_name='Раздел', related_name="resp_group")
    
    class Meta:

        verbose_name = 'Ответственность'
        verbose_name_plural = 'Ответственности'
    def __str__(self):
            return str(self.resp)
    
class Safety_Commitee(models.Model):
    type =  models.ForeignKey('SafetyType', models.DO_NOTHING, null=True, verbose_name='Раздел', related_name="type_comm")
    comm = models.ForeignKey('commeteresp.Committee1', models.DO_NOTHING, null=True, verbose_name='Раздел', related_name="comm_group")

    class Meta:

        verbose_name = 'Комиссия'
        verbose_name_plural = 'Комиссии'
    def __str__(self):
            return str(self.comm)





# Общая модель для раздела "Безопасность"
class SafetyFile(models.Model):
    name = models.CharField(verbose_name='Имя документа', max_length=255)
    url = models.FileField(verbose_name='Путь до файла',upload_to='safety')
    chapter = models.ForeignKey('SafetyType', models.DO_NOTHING, null=True, verbose_name='Раздел', related_name="mainpage_file")
    # category = models.ForeignKey('SafetyDocumentCategory', models.DO_NOTHING, null=True, verbose_name='Категория документа')
    # formainpage = models.BooleanField(default=False, verbose_name="Основная информация")
    # sign_date = models.DateField(verbose_name='Дата документа')
    # created_at = models.DateTimeField(verbose_name='Дата загрузки файла', auto_now_add=True)
    # update_at = models.DateTimeField(verbose_name='Дата обновления файла', auto_now=True)

    class Meta:

        verbose_name = 'Документ для главной'
        verbose_name_plural = 'Документы для главной'

    def __str__(self):
        return str(self.name)