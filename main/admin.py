from django.contrib import admin
from main.models import *

class WorksAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'finished', 'day']
    list_display = ('id', 'name', 'finished', 'day')

admin.site.register(Works, WorksAdmin)