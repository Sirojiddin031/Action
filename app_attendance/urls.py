from django.urls import path
from .views import (
    AttendanceListCreateView, AttendanceDetailView,
    AttendanceLevelListCreateView, AttendanceLevelDetailView
)

urlpatterns = [
    # Attendance APIs
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),

    # Attendance Level APIs
    path('attendance-level/', AttendanceLevelListCreateView.as_view(), name='attendance-level-list-create'),
    path('attendance-level/<int:pk>/', AttendanceLevelDetailView.as_view(), name='attendance-level-detail'),
]
