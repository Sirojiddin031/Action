 # app_attendance/models.py

from django.db import models
from app_users.models import Student

# Yo‘qlama darajasi
class AttendanceLevel(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

# Yo‘qlama
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.ForeignKey(AttendanceLevel, on_delete=models.RESTRICT)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')]
    )
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # ✅ 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.phone} - {self.date} - {self.status}"

# from django.db import models
# from app_users.models import Student

# class Attendance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     date = models.DateField()
#     status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
    
#     def __str__(self):
#         return f"{self.student.user.phone} - {self.date} - {self.status}"

# Create your models here.
