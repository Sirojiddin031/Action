
from django.contrib import admin
from .models import Student, Parents, Worker, Staff, Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated')
    filter_horizontal = ('departments', 'course') 


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'grade', 'created']
    search_fields = ['user__username', 'grade']

@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'student')
    search_fields = ('student__user__username', 'phone_number')

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'salary', 'created')
    search_fields = ('user__username', 'position')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ('user__username', 'department')

