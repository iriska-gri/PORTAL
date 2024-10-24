from django.db import models
from django.conf import settings
from accounts.models import User
# Create your models here.
import pandas as pd

class Pages(models.Model):
    page = models.CharField(max_length=255)
    fullPath = models.CharField(max_length=255)
    ico = models.CharField(verbose_name='Иконка', max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.page)    


class CountVisitor(models.Model):
    # page = models.CharField(db_index=True, max_length=255) 
    pages = models.ForeignKey(Pages, on_delete=models.PROTECT, related_name='get_pages', verbose_name='Страница', null=True)
    visitdate = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Пользователь', null=True, blank=True)
    count = models.IntegerField(default=0)
    # fullPath = models.CharField(max_length=255) 
    # ico = models.CharField(verbose_name='Иконка', max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.pages)
    

    
    # class Meta:
     
        
        # constraints = [
        #     models.UniqueConstraint(fields=['page', 'user', 'visitdate', 'fullPath', 'ico'], name='unique appversion')
        # ]
    
    
   