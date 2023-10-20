from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Создаем менеджер пользователей для модели CustomUser
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Проверяем, что email указан
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)  # Нормализуем email
        user = self.model(email=email, **extra_fields)  # Создаем пользователя с указанными данными
        user.set_password(password)  # Устанавливаем пароль
        user.save(using=self._db)  # Сохраняем пользователя
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Создаем суперпользователя с правами администратора
        extra_fields.setdefault('is_staff', True)  # Устанавливаем флаг "is_staff" в True
        extra_fields.setdefault('is_superuser', True)  # Устанавливаем флаг "is_superuser" в True

        return self.create_user(email, password, **extra_fields)

# Определяем модель CustomUser, основанную на AbstractBaseUser и PermissionsMixin
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Поле для адреса электронной почты
    is_staff = models.BooleanField(default=False)  # Флаг, определяющий, является ли пользователь сотрудником
    is_active = models.BooleanField(default=True)  # Флаг, определяющий, активен ли пользователь

    objects = CustomUserManager()  # Устанавливаем менеджер CustomUserManager для пользователей

    USERNAME_FIELD = 'email'  # Поле, используемое для идентификации пользователя (email)

    def __str__(self):
        return self.email

# Определяем модель Document для хранения документов
class Document(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Связь с пользователем, который загрузил документ
    name = models.CharField(max_length=255)  # Поле для названия документа
    description = models.TextField()  # Поле для описания документа
    file = models.FileField(upload_to='documents/')  # Поле для загрузки файла документа с указанием директории

    def __str__(self):
        return self.name  # Возвращаем название документа в виде строки в админ панеле