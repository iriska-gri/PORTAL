from django.db import models
from django.conf import settings
from userauth.models import DictEmployee

class BasePosition(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150, blank=True, db_index=True)
    order = models.IntegerField(blank=True, null=True, verbose_name='Сортировка')

    class Meta:
        # ЕО - ежедневный обход
  
        verbose_name = "Справочник - Статус сотрудников"
        verbose_name_plural = "Справочник - Статус сотрудников"    

    def __str__(self):
        return str(self.name)
    
class DailyRoundUp(models.Model):
    todaysDate =  models.DateField(verbose_name='Начало рабочего периода')
    user = models.CharField(max_length=100, verbose_name='Логин')
    position = models.ForeignKey(BasePosition, on_delete=models.PROTECT, related_name="get_position", verbose_name='Позиция')

    class Meta:

        verbose_name = "Ежедневный обход"
        verbose_name_plural = "Ежедневный обход"    

    def __str__(self):
        return str(self.position)

class GeneralVacation(models.Model):
    CHOICES = (
            ('os', 'Осн'),
            ('nd', 'Доп н/д'),
            ('vl', 'Доп в/л'),
        )
 
    login = models.CharField(max_length=100, blank=True, null=True, verbose_name='Логин')
    planned_date = models.DateField(verbose_name='Запланированная дата')
    count_days = models.IntegerField(verbose_name='Кол-во дней', default=0, blank=True)
    type_of_vacation = models.CharField(max_length=300, choices = CHOICES, verbose_name='Тип отпуска')
    start_work_period = models.DateField(verbose_name='Начало рабочего периода')
    end_work_period = models.DateField(verbose_name='Конец рабочего периода', blank=True, null=True)

    class Meta:
  
        verbose_name = "График отпусков"
        verbose_name_plural = "График отпусков"

    def __str__(self):
        return str(self.login)
    
    # def department(self):
    #     return DictEmployee.objects.using('user_directory').get(login=self.username).department
    
class PlanCalendar(models.Model):
    name = models.CharField(verbose_name='Название', max_length=500, blank=True, db_index=True)
    start_work_period = models.DateField(verbose_name='Начало рабочего периода')
    end_work_period = models.DateField(verbose_name='Конец рабочего периода', blank=True, null=True)

    class Meta:

        verbose_name = "План-график"
        verbose_name_plural = "План-график"
    
    def __str__(self):
        return str(self.name)
    


    

