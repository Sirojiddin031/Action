
# app_users/urls.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WorkerViewSet, StudentViewSet, ParentsViewSet, StaffViewSet,
    WorkerListCreateView, WorkerDetailView,
    StudentListCreateView, StudentDetailView,
    StaffListCreateView, StaffDetailView,
    ParentsListCreateView, ParentsDetailView,
    TeacherViewSet, TeacherListCreateView, TeacherDetailView,
    get_students
)

# **ViewSet-lar uchun Router**
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'parents', ParentsViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'teachers', TeacherViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # ViewSet API
    path('', include(router.urls)),  # DRF ViewSet-lar uchun
    
    path('teachers/list/', TeacherListCreateView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    
    path('api/students/', StudentListCreateView.as_view(), name='student-list'),
    path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    path('api/parents/', ParentsListCreateView.as_view(), name='parents-list'),
    path('api/parents/<int:pk>/', ParentsDetailView.as_view(), name='parents-detail'),
    
    path('api/workers/', WorkerListCreateView.as_view(), name='worker-list'),
    path('api/workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    
    path('api/staff/', StaffListCreateView.as_view(), name='staff-list'),
    path('api/staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('api/get_students/', get_students, name='get_students'),  # Function-based API
       # JWT autentifikatsiya
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

