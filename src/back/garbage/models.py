# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Carousels(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    link = models.ImageField(upload_to='fns/%Y/%m/%d', default="newsimage/default.jpg", null=True, verbose_name='Картинка')
    order = models.IntegerField(blank=True, null=True)
    link2 = models.ImageField(upload_to='fns/%Y/%m/%d', null=True, verbose_name='Картинка2')
    class Meta:
        managed = False
        db_table = 'carousels'

    def __str__(self):
        return str(self.title)
