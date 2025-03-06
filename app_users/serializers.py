from rest_framework import serializers
from .models import Student, Parents, Worker, Staff, Teacher, User
from app_courses.models import Course
from app_auth.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {"password": {"write_only": True}}

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherDetailSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject', 'created']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'




class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Yangi foydalanuvchi yaratish uchun

    class Meta:
        model = Student
        fields = ["id", "position", "salary", "user", "courses"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")  # User malumotlarini ajratib olish
        user = User.objects.create_user(**user_data)  # Yangi user yaratish
        student = Student.objects.create(user=user, **validated_data)  # Student yaratish
        return student



class ParentsSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Parents
        fields = ['id', 'student', 'full_name', 'phone_number', 'address', 'descriptions', 'created', 'updated']





class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Staff
        fields = ['id', 'user', 'department']