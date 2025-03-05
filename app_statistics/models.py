# app_statistics/models.py
from django.db import models
from app_courses.models import Course

class Statistic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_students = models.IntegerField()
    average_attendance = models.FloatField()
    
    def __str__(self):
        return self.course.title

# Create your models here.
