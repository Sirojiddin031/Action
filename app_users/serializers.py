from rest_framework import serializers
from .models import Student, Parents, Worker, Staff, Teacher
from app_courses.models import Course
from app_auth.models import CustomUser


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'grade', 'courses', 'created']

class ParentsSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Parents
        fields = ['id', 'student', 'full_name', 'phone_number', 'address', 'descriptions', 'created', 'updated']

class WorkerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    courses = CourseSerializer(many=True)

    class Meta:
        model = Worker
        fields = ['id', 'user', 'position', 'salary', 'courses', 'created']

class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Staff
        fields = ['id', 'user', 'department']
