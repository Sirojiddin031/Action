# app_auth/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, TokenModel


class UserSerializer(serializers.ModelSerializer):
    """Foydalanuvchi ma'lumotlarini olish uchun serializer"""
    class Meta:
        model = User
        fields = ["id", "phone", "full_name", "is_student", "is_teacher", "is_active", "is_staff"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """JWT Token olish uchun maxsus serializer"""
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        if not user.is_active:
            raise serializers.ValidationError({"detail": "Foydalanuvchi faollashtirilmagan."})

        data["full_name"] = user.full_name
        return data


class RegisterSerializer(serializers.ModelSerializer):
    """Foydalanuvchini ro‘yxatdan o‘tkazish uchun serializer"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "phone", "full_name", "password"]

    def create(self, validated_data):
        """Foydalanuvchini yaratish"""
        user = User.objects.create_user(
            phone=validated_data["phone"],
            full_name=validated_data["full_name"],
            password=validated_data["password"]
        )
        user.is_active = True  # Foydalanuvchini avtomatik faollashtirish
        user.save()
        return user

class TokenModelSerializer(serializers.ModelSerializer):
    token = serializers.CharField(min_length=1, required=True) 
    
    class Meta:
        model = TokenModel
        fields = '__all__'

