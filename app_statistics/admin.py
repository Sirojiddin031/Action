
from django.contrib import admin
from .models import Statistic

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('course', 'total_students', 'average_attendance')
    search_fields = ('course__title',)

# Register your models here.
