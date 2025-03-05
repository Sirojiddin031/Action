# app_auth/urls.py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    RegisterView,
    UserListCreateView,
    UserDetailView,
    TokenModelViewSet
)

router = DefaultRouter()
router.register(r'tokens', TokenModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("users/", UserListCreateView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),

    path("register/", RegisterView.as_view(), name="register"), 
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
