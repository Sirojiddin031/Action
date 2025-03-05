from django.contrib import admin
from .models import Course, Day, Room, TableType, Table, Group, Topic, GroupHomework, Homework
from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions']  # 'name' ni olib tashladik

admin.site.register(Course, CourseAdmin)

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(TableType)
class TableTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'room', 'type')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'start_date', 'end_date', 'price')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'is_active')

@admin.register(GroupHomework)
class GroupHomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'group', 'topic', 'is_active')

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')



# Register your models here.
