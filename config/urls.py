
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger konfiguratsiyasi
schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="This is an API for user authentication and attendance management.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # Django admin panel
   path('admin/', admin.site.urls),
   path('', home, name='home'), 
   
   # App routes
   path('api/courses/', include('app_courses.urls')),
   path('api-auth/', include('rest_framework.urls')),  # DRF login paneli
   path('api/attendance/', include('app_attendance.urls')),  # Yo‘qlama 
   path('api/users/', include('app_users.urls')),  
   path('users/', include('app_users.urls')),
   path('api/auth/', include('app_auth.urls')),  # Auth (ro‘yxatdan o‘tish, login)

   # JWT Token olish va yangilash
   path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
   # API Documentation (Swagger & Redoc)
   path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

