from django.db import models

# Create your models here.
class Committee1(models.Model):
    id= models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True, db_comment='═ршьхэютрэшх ъюьшёёшш',verbose_name = 'Название')
    num_start = models.CharField(max_length=100, blank=True, null=True, db_comment='═юьхЁ яЁшърчр ю ёючфрэшш ъюьшёёшш')
    date_start = models.DateField(blank=True, null=True, db_comment='─рЄр яЁшърчр ю ёючфрэшш ъюьшёёшш')
    num_finish = models.CharField(max_length=100, blank=True, null=True, db_comment='═юьхЁ яЁшърчр юс єяЁрчфэхэшш ъюьшёёшш')
    date_finish = models.DateField(blank=True, null=True, db_comment='─рЄр єяЁрчфэхэш  ъюьшёёшш')
    comment = models.CharField(max_length=4000, blank=True, null=True, db_comment='╧Ёшьхўрэшх')
    id_dict_committee_type = models.ForeignKey('DictCommitteeType', models.DO_NOTHING, db_column='id_dict_committee_type', db_comment='╙эшъры№э√щ эюьхЁ тшфр ъюьшёёшш',verbose_name = 'Тип')
    id_master = models.ForeignKey('self', models.DO_NOTHING, db_column='id_master', blank=True, null=True, db_comment='╙═ т√°хёЄю ∙хщ ъюьшёёшш',verbose_name = 'Комиссия-родитель')

    class Meta:
        managed = False
        db_table = 'committee1'
        db_table_comment = '╤яшёюъ ъюьшёёшщ'
        verbose_name = 'Комиссия'
        verbose_name_plural = 'Комиссии'

    def __str__(self):
        return str(self.name)


class Committee1Files(models.Model):
    id= models.PositiveIntegerField(primary_key=True)
    id_committee1 = models.ForeignKey(Committee1, models.DO_NOTHING, db_column='id_committee1', db_comment='╚─ ъюьшёёшш',related_name='comitee_files')
    file_name = models.FileField(null=True, blank=True, upload_to='comitee_files')
    # file_name = models.CharField(max_length=1024, db_comment='╚ь  Їрщыр')
    is_actual = models.IntegerField(db_comment='╧Ёшчэръ ръЄєры№эюёЄш Їрщыр',verbose_name = 'Актуальность')

    class Meta:
        managed = False
        db_table = 'committee1_files'
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return str(self.file_name)
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)


class Committee2(models.Model):
    id_committee1 = models.ForeignKey(Committee1, models.DO_NOTHING, db_column='id_committee1', db_comment='╙эшъры№э√щ эюьхЁ ъюьшёёшш', related_name='com_members')
    committee_position = models.ForeignKey('DictCommitteePosition', models.DO_NOTHING, db_column='id_dict_committee_position', db_comment='╙эшъры№э√щ эюьхЁ фюцэюёЄш т ъюьшёёшш',verbose_name = 'Роль')
    employee = models.ForeignKey('userauth.DictEmployee', models.DO_NOTHING, db_column='id_dict_employee', blank=True, null=True, db_comment='╚─ ёюЄЁєфэшър', related_name="user_committe2",verbose_name = 'Участник')
    committee_expert = models.ForeignKey('DictCommitteeExpert', models.DO_NOTHING, db_column='id_dict_committee_expert', blank=True, null=True, db_comment='╙эшъры№э√щ эюьхЁ ¤ъёяхЁЄр')

    class Meta:
        managed = False
        db_table = 'committee2'
        db_table_comment = '╤юёЄрт ъюьшёёшщ'
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return str(self.committee_position.name)

class DictCommitteeExpert(models.Model):
    fio = models.CharField(max_length=250, blank=True, null=True, db_comment='╘╚╬ ¤ъёяхЁЄр')
    tel = models.CharField(max_length=100, blank=True, null=True, db_comment='╥хыхЇюэ')

    class Meta:
        managed = False
        db_table = 'dict_committee_expert'
        db_table_comment = '╤яЁртюўэшъ эхчртшёшь√ї ¤ъёяхЁЄют'
    
    def __str__(self):
        return str(self.fio)


class DictCommitteeOrderAddon(models.Model):
    id_committee1 = models.ForeignKey(Committee1, models.DO_NOTHING, db_column='id_committee1', db_comment='╚─ ъюьшёёшш, т яЁшърчх яю ъюЄюЁющ яЁюшчю°ыш шчьхэхэш ')
    number = models.CharField(max_length=100, db_comment='═юьхЁ шчьхэхэшщ ъ яЁшърчє ю ъюьшёёшш')
    date = models.DateField(db_comment='─рЄр шчьхэхэшщ т яЁшърч ю ъюьшёёшш')
    name = models.CharField(max_length=1024, blank=True, null=True, db_comment='═ршьхэютрэшх шчьхэхэшщ ъ яЁшърчє ю ъюьшёёшш')
    text = models.TextField(blank=True, null=True, db_comment='╥хъёЄ шчьхэхэшщ т яЁшърч ю ъюьшёёшш')

    class Meta:
        managed = False
        db_table = 'dict_committee_order_addon'
        db_table_comment = '╥рсышЎр фюяюыэхэшщ ъ яЁшърчє ю ъюьшёёшш'



class DictCommitteePosition(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='эршьхэютрэшх фюцэюёЄш т ъюьшёёшш')
    name_short = models.CharField(max_length=100, blank=True, null=True, db_comment='ъЁрЄъюх эршьхэютрэшх фюцэюёЄш т ъюьшёёшш')
    ord = models.IntegerField(blank=True, null=True, db_comment='╧юЁ фюъ ёюЁЄшЁютъш')

    class Meta:
        managed = False
        db_table = 'dict_committee_position'
        db_table_comment = '╤яЁртюўэшъ фюыцэюёЄхщ ъюьшёёшщ'

    def __str__(self):
        return str(self.name_short)


class DictCommitteeType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='═ршьхэютрэшх тшфр ъюьшёёшш')

    class Meta:
        managed = False
        db_table = 'dict_committee_type'
        db_table_comment = '╤яЁртюўэшъ тшфют ъюьшёёшщ'

    def __str__(self):
        return str(self.name)
    

class OrderResponsibility(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_comment='╥рсхы№э√щ эюьхЁ')
    number = models.CharField(max_length=50, db_comment='═юьхЁ яЁшърчр')
    date = models.DateField(db_comment='─рЄр яЁшърчр')
    name = models.CharField(max_length=1024, db_comment='═рчтрэшх яЁшърчр')
    sphere_of_responsibility = models.CharField(max_length=1024, db_comment='╤ЇхЁр юЄтхЄёЄтхээюёЄш ёюЄЁєфэшъют, эрчэрўрхьр  фрээ√ь яЁшърчюь')

    class Meta:
        managed = False
        db_table = 'order_responsibility'
        db_table_comment = '╥рсышЎр яЁшърчют ю эрчэрўхэшш юЄтхЄёЄтхээ√ї ёюЄЁєфэшъют'
        verbose_name = 'Cфера ответственности'
        verbose_name_plural = 'Сферы ответстсвенности'
    def __str__(self):
        return f'{self.number} - {self.name}'

class OrderResponsibilityEmployee(models.Model):
    id_order_responsibility = models.ForeignKey(OrderResponsibility, models.DO_NOTHING, db_column='id_order_responsibility', primary_key=True, db_comment='╚─ яЁшърчр ю эрчэрўхэшш юЄтхЄёЄтхээ√ї ёюЄЁєфэшъют',related_name="respons_users")  # The composite primary key (id_order_responsibility, id_dict_employee) found, that is not supported. The first column is selected.
    employee = models.ForeignKey('userauth.DictEmployee', models.DO_NOTHING, db_column='id_dict_employee', db_comment='╚─ ёюЄЁєфэшър, ъюЄюЁ√щ эрчэрўхэ юЄтхЄёЄтхээ√ь яю фрээюьє яЁшърчє', related_name="user_respons")

    class Meta:
        managed = False
        db_table = 'order_responsibility_employee'
        unique_together = (('id_order_responsibility', 'employee'),)
        verbose_name = 'Ответственный сотрудник'
        verbose_name_plural = 'Ответственные сотрудники'
    def __str__(self):
        return str(self.employee)
class OrderResponsibilityFiles(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_comment='╥рсхы№э√щ эюьхЁ')
    id_order_responsibility = models.ForeignKey(OrderResponsibility, models.DO_NOTHING, db_column='id_order_responsibility', db_comment='╚─ яЁшърчр юс юЄтхЄёЄтхээ√ї ёюЄЁєфэшърї', related_name="get_resp_files")
    file_name = models.FileField(null=True, blank=True, upload_to='resp_files')
    is_actual = models.IntegerField(db_comment='╧Ёшчэръ ръЄєры№эюёЄш Їрщыр')

    class Meta:
        managed = False
        db_table = 'order_responsibility_files'
        verbose_name = 'Файл сферы ответственности'
        verbose_name_plural = 'Файлы сферы ответственности'



    def __str__(self):
        return f'{self.file_name}'