from documents import views  # Импортируем представления из нашего приложения documents.
from rest_framework.routers import DefaultRouter  # Импортируем DefaultRouter из Django REST framework.

router = DefaultRouter()  # Создаем экземпляр DefaultRouter, который поможет нам автоматически создать URL-маршруты для представлений.

router.register('document', views.DocumentViewSet)  # Регистрируем наше представление DocumentViewSet под именем 'document' в нашем роутере.

urlpatterns = [

]  # Инициализируем список URL-маршрутов, который будем использовать в нашем проекте.

urlpatterns += router.urls  # Добавляем URL-маршруты, созданные нашим роутером, к списку URL-маршрутов проекта.

