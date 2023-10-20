from rest_framework import serializers
from .models import Document, CustomUser

# Сериализатор для модели CustomUser, используется для преобразования данных пользователя в JSON
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Пароль должен быть записываемым, но не отображаться при сериализации

    class Meta:
        model = CustomUser  # Указываем модель, с которой работает этот сериализатор
        fields = ['email', 'password']  # Указываем поля модели, которые будут сериализованы

# Сериализатор для модели Document, используется для преобразования данных документов в JSON
class DocumentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')  # Задаем поле "user" как только для чтения и указываем источник данных (email пользователя)

    class Meta:
        model = Document  # Указываем модель, с которой работает этот сериализатор
        fields = '__all__'  # Сериализуем все поля модели Document
