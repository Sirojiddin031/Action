
from rest_framework import serializers
from .models import Attendance, AttendanceLevel

class AttendanceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLevel
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.phone', read_only=True)
    level_title = serializers.CharField(source='level.title', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'student_name', 'level', 'level_title', 'date', 'status', 'created', 'updated']
