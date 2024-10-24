from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display=('username','names', 'is_active', 'is_staff')
    search_fields = ('username',)
    ordering=('username',)

    # fields=(('user', 'username'), 'is_active', 'is_staff', 'updated_at',)



admin.site.register(User, UserAdmin)