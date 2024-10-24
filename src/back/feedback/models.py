from django.db import models
from django.conf import settings
from userauth.models import DictEmployee

class BaseCriteria(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150, blank=True, db_index=True)
    ico = models.CharField(verbose_name='Иконка', max_length=150, null=True, blank=True)
    rating = models.IntegerField(verbose_name='Рейтинг', default=5, blank=True)
    color = models.CharField(verbose_name='Цвет иконки', max_length=150, null=True, blank=True)
    class Meta:
      
            verbose_name = "Справочник - Критерии оценки"
            verbose_name_plural = "Справочник -  Критерии оценки"
    def __str__(self):
        return str(self.name)
    
# Первичная модель
class UserComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.PROTECT, related_name='get_userauth', verbose_name='Пользователь')
    time_create = models.DateTimeField(auto_now_add = True, verbose_name='Время создания')
    comment = models.TextField(null=True, verbose_name='Комментарий')
    utility = models.BooleanField(default=True, verbose_name='Полезность')

    class Meta:
     
            verbose_name = "Комментарий пользователя"
            verbose_name_plural = "Комментарии пользователя"

    def __str__(self):
        return str(self.user.fio())

    def names(self):
        return DictEmployee.objects.get(login=self.user)
    
    names.short_description="ФИО"

# Дочерняя модель
class RatingStatus(models.Model):
    crit = models.ForeignKey(BaseCriteria, on_delete=models.PROTECT, related_name='get_criteria', verbose_name='Критерий')
    rating = models.FloatField(verbose_name='Рейтинг')
    usercom = models.ForeignKey(UserComment, on_delete=models.PROTECT, related_name='get_rating', verbose_name='Комментарий')

    class Meta:
     
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return str(self.crit)
    

