from django.conf.urls.static import static  # Импортируем функцию для обработки медиа-файлов
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from configs import settings  # Импортируем настройки проекта
from documents.views import UserRegistrationView  # Импортируем представление для регистрации пользователей

# Определяем URL-маршруты приложения
urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели Django
    path('api/', include('documents.urls')),  # URL-маршруты для API, определенные в приложении documents
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL для получения JWT-токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # URL для обновления JWT-токена
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),  # URL для регистрации нового пользователя
]

# Добавляем обработку медиа-файлов. Это важно для отображения файлов, загруженных пользователями.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
