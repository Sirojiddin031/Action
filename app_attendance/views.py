from django.shortcuts import render
from rest_framework import generics
from .models import Attendance, AttendanceLevel
from .serializers import AttendanceSerializer, AttendanceLevelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class AttendanceView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        return Response({"message": "Attendance recorded!"})

# Attendance CRUD API
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# AttendanceLevel CRUD API
class AttendanceLevelListCreateView(generics.ListCreateAPIView):
    queryset = AttendanceLevel.objects.all()
    serializer_class = AttendanceLevelSerializer

class AttendanceLevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceLevel.objects.all()
    serializer_class = AttendanceLevelSerializer

# Create your views here.
