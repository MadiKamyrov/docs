from django.contrib import admin  # Импортируем модуль для работы с административной панелью Django
from .models import CustomUser, Document  # Импортируем модели, которые мы хотим зарегистрировать в административной панели

# Регистрируем модели в административной панели
admin.site.register(CustomUser)  # Регистрируем модель CustomUser, чтобы ее можно было управлять в административной панели
admin.site.register(Document)  # Регистрируем модель Document, чтобы ее можно было управлять в административной панели
