
from django.db import models
from app_courses.models import Course  
from app_auth.models import CustomUser  
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departments = models.ManyToManyField('app_users.Departments', related_name='teacher')  #
    course = models.ManyToManyField(Course, related_name="teacher")  #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def get_departments(self):
        Departments = apps.get_model('app_users', 'Departments')  # 
        return Departments.objects.filter(teacher=self)

    def __str__(self):
        return self.user.phone


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    grade = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, related_name="students")  # ✅ 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.grade}"


class Parents(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="parents")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Worker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="worker_profile")
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    courses = models.ManyToManyField(Course, related_name="workers")  # ✅ 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="staff_profile")
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.department}"

class Departments(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
