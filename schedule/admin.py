from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['date','startTime','endTime']

# Register your models here.
admin.site.register(Schedule,ScheduleAdmin)

