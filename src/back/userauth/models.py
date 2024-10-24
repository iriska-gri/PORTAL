# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models






class DictCompetences(models.Model):
    id_dict_competences_type = models.ForeignKey('DictCompetencesType', models.DO_NOTHING, db_column='id_dict_competences_type', db_comment='шфхэЄшЇшърЄюЁ уЁєяя√ ъюьяхЄхэЎшш')
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dict_competences'
        db_table_comment = '╤яЁртюўэшъ ъюьяхЄхэЎшщ'


class DictCompetencesType(models.Model):
    name = models.CharField(max_length=50, db_comment='═ршьхэютрэшх уЁєяя√ ъюьяхЄхэЎшщ')

    class Meta:
        managed = False
        db_table = 'dict_competences_type'
        db_table_comment = '├Ёєяя√ ъюьяхЄхэЎшщ'


class DictDepartment(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_comment='╥рсхы№э√щ эюьхЁ')
    id_curator = models.ForeignKey('DictEmployee', models.DO_NOTHING, db_column='id_curator', blank=True, null=True, db_comment='╚─ ъєЁрЄюЁр юЄфхыр', related_name='deps_curator')
    id_chief = models.ForeignKey('DictEmployee', models.DO_NOTHING, db_column='id_chief', related_name='dictdepartment_id_chief_set', blank=True, null=True, db_comment='╚─ эрўры№эшър юЄфхыр')
    name = models.CharField(max_length=500, db_comment='═рчтрэшх юЄфхыр')
    deleted = models.IntegerField(db_comment='╠рЁъх єфрыхэш  чряшёш')
    name_from_ad = models.CharField(db_column='name_from_AD', max_length=500, blank=True, null=True, db_comment='═рчтрэшх юЄфхыр т AD')  # Field name made lowercase.
    name_position_chief = models.CharField(max_length=500, db_comment='═рчтрэшх фюыцэюёЄш эрўры№эшър юЄфхыр')
    code_department = models.CharField(max_length=2)
    order_department = models.IntegerField()

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        managed = False
        db_table = 'dict_department'
        db_table_comment = '╤яЁртюўэшъ юЄфхыют'
    def __str__(self):
        return str(self.name)

class DictEmployee(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_comment='╥рсхы№э√щ эюьхЁ')
    id_dict_department = models.ForeignKey(DictDepartment, models.DO_NOTHING, db_column='id_dict_department', related_name='dep_user', db_comment='╚─ юЄфхыр, т ъюЄюЁюь ЁрсюЄрхЄ ёюЄЁєфэшъ')
    id_dict_position = models.ForeignKey('DictPosition', models.DO_NOTHING, db_column='id_dict_position', db_comment='╚─ чрэшьрхьющ фюыцэюёЄш', related_name='ord_position')
    login = models.CharField(max_length=100, blank=True, null=True, db_comment='ыюушэ(sAMAccountName)')
    password = models.CharField(max_length=100, blank=True, null=True, db_comment='╧рЁюы№ фы  тїюфр эр яюЁЄры')
    fio = models.CharField(db_column='FIO', max_length=300, blank=True, null=True, db_comment='╘╚╬(cn)')  # Field name made lowercase.
    familyname = models.CharField(max_length=100, blank=True, null=True, db_comment='╘рьшыш (sn)')
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='╚ь ')
    parentname = models.CharField(max_length=100, blank=True, null=True, db_comment='╬ЄўхёЄтю')
    department = models.CharField(max_length=500, blank=True, null=True, db_comment='╬Єфхы(department)')
    post = models.CharField(max_length=500, blank=True, null=True, db_comment='фюыцэюёЄ№(title)')
    room = models.CharField(max_length=20, blank=True, null=True, db_comment='ърсшэхЄ(physicalDeliveryOfficeName)')
    email = models.CharField(max_length=100, blank=True, null=True, db_comment='рфЁхё ¤ыхъЄЁюээющ яюўЄ√(mail)')
    tel = models.CharField(max_length=20, blank=True, null=True, db_comment='уюЁюфёъющ ЄхыхЇюэ(telephoneNumber)')
    iptel = models.CharField(max_length=20, blank=True, null=True, db_comment='тэєЄЁхээшщ ЄхыхЇюэ(OfficePhone)')
    workstatus = models.CharField(db_column='WorkStatus', max_length=500, blank=True, null=True, db_comment='ёЄрЄєё')  # Field name made lowercase.
    is_curator = models.PositiveIntegerField(db_comment='╠рЁъхЁ ъєЁрЄюЁр')
    datebegin = models.DateField(db_column='DateBegin', blank=True, null=True, db_comment='─рЄр яЁшхьр эр ЁрсюЄє')  # Field name made lowercase.
    dateend = models.DateField(db_column='DateEnd', blank=True, null=True, db_comment='─рЄр єтюы№эхэш ')  # Field name made lowercase.
    workstatus2 = models.CharField(db_column='WorkStatus2', max_length=500, blank=True, null=True, db_comment='ёЄрЄєё єўхЄэющ чряшёш(Enabled)')  # Field name made lowercase.
    # workstatus3 = models.TextField(db_column='WorkStatus3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deleted = models.PositiveIntegerField(db_comment='╠рЁъхЁ єфрыхэш ')
    deleteddate = models.DateField(db_column='deletedDate', blank=True, null=True, db_comment='─рЄр чряюыэхэш  ьрЁъхЁр єфрыхэш ')  # Field name made lowercase.
    is_responsible = models.PositiveIntegerField(db_comment='╙фрышЄ№')
    is_changed = models.PositiveIntegerField(db_comment='╧Ёшчэръ эрышўш  шчьхэхэшщ')
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True, db_comment='─рЄр Ёюцфхэш  ёюЄЁєфэшър')  # Field name made lowercase.
    lotus =  models.CharField(db_column='lotus', max_length=200, blank=True, null=True, db_comment='ёЄрЄєё єўхЄэющ чряшёш(Enabled)')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dict_employee'
        db_table_comment = '╤яшёюъ ёюЄЁєфэшъют'

    def __str__(self):
        return str(self.fio)


class DictPosition(models.Model):
    name = models.CharField(max_length=1024, db_comment='═ршьхэютрэшх фюыцэюёЄш')
    order_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dict_position'
        db_table_comment = '╤яЁртюўэшъ фюыцэюёЄхщ'

    def __str__(self):
        return str(self.name)



class MatrixCompetences(models.Model):
    id_dict_employee = models.ForeignKey(DictEmployee, models.DO_NOTHING, db_column='id_dict_employee', db_comment='шфхэЄшЇшърЄюЁ ёюЄЁєфэшър')
    id_dict_competences = models.ForeignKey(DictCompetences, models.DO_NOTHING, db_column='id_dict_competences', db_comment='шфхэЄшЇшърЄюЁ ъюьяхЄхэЎшш')

    class Meta:
        managed = False
        db_table = 'matrix_competences'
        db_table_comment = '╠рЄЁшЎр ъюьяхЄхэЎшщ'



class Sprstaff(models.Model):
    tn = models.SmallIntegerField(primary_key=True, db_comment='╥рсхы№э√щ эюьхЁ')
    login = models.CharField(max_length=100, blank=True, null=True, db_comment='ыюушэ(sAMAccountName)')
    fio = models.CharField(db_column='FIO', max_length=300, blank=True, null=True, db_comment='╘╚╬(cn)')  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=100, blank=True, null=True, db_comment='╘рьшыш (sn)')  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=100, blank=True, null=True, db_comment='╚ь ')  # Field name made lowercase.
    o = models.CharField(db_column='O', max_length=100, blank=True, null=True, db_comment='╬ЄўхёЄтю')  # Field name made lowercase.
    department = models.CharField(max_length=500, blank=True, null=True, db_comment='╬Єфхы(department)')
    post = models.CharField(max_length=500, blank=True, null=True, db_comment='фюыцэюёЄ№(title)')
    room = models.CharField(max_length=20, blank=True, null=True, db_comment='ърсшэхЄ(physicalDeliveryOfficeName)')
    email = models.CharField(max_length=50, blank=True, null=True, db_comment='рфЁхё ¤ыхъЄЁюээющ яюўЄ√(mail)')
    tel = models.CharField(max_length=20, blank=True, null=True, db_comment='уюЁюфёъющ ЄхыхЇюэ(telephoneNumber)')
    iptel = models.CharField(max_length=20, blank=True, null=True, db_comment='тэєЄЁхээшщ ЄхыхЇюэ(OfficePhone)')
    workstatus = models.CharField(db_column='WorkStatus', max_length=500, blank=True, null=True, db_comment='ёЄрЄєё')  # Field name made lowercase.
    datebegin = models.DateField(db_column='DateBegin', blank=True, null=True, db_comment='─рЄр яЁшхьр эр ЁрсюЄє')  # Field name made lowercase.
    dateend = models.DateField(db_column='DateEnd', blank=True, null=True, db_comment='─рЄр єтюы№эхэш ')  # Field name made lowercase.
    workstatus2 = models.CharField(db_column='WorkStatus2', max_length=500, blank=True, null=True, db_comment='ёЄрЄєё єўхЄэющ чряшёш(Enabled)')  # Field name made lowercase.
    workstatus3 = models.TextField(db_column='WorkStatus3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sprstaff'
        db_table_comment = '╤яшёюъ ёюЄЁєфэшъют'


class Table14(models.Model):
    fio = models.CharField(db_column='FIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col_2 = models.CharField(db_column='COL 2', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_3 = models.CharField(db_column='COL 3', max_length=22, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_4 = models.CharField(db_column='COL 4', max_length=23, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_5 = models.CharField(db_column='COL 5', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_6 = models.CharField(db_column='COL 6', max_length=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_7 = models.CharField(db_column='COL 7', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_8 = models.CharField(db_column='COL 8', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'table 14'
