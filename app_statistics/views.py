from django.shortcuts import render
from rest_framework import viewsets
from .models import Statistic
from .serializers import StatisticSerializer

class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

# Create your views here.
