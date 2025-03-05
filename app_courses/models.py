from django.db import models
from django.apps import apps


# Markazda o‘qitiladigan fanlar
class Course(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  # name maydonini qo‘shamiz
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title



class Day(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class TableType(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Table(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.RESTRICT, related_name="tables")
    type = models.ForeignKey(TableType, on_delete=models.RESTRICT, related_name="tables")
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Group(models.Model):
    title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')
    teachers = models.ManyToManyField('app_users.Worker', related_name='groups')  # Worker modeli app_users ichida
    table = models.ForeignKey(Table, on_delete=models.RESTRICT, related_name='groups')
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name="topics")
    is_active = models.BooleanField(default=True)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class GroupHomework(models.Model):
    title = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name="homeworks")
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT, related_name="homeworks")
    is_active = models.BooleanField(default=True)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.group} - {self.topic}"


class Homework(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# Dynamic model loading via `apps.get_model`
def get_worker_model():
    return apps.get_model('app_users', 'Worker')


def get_course_objects():
    Course = apps.get_model('app_courses', 'Course')
    return Course.objects.all()
