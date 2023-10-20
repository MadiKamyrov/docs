from rest_framework import permissions

# Создаем собственное правило доступа, которое позволяет только владельцу объекта выполнять изменения
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Если запрос выполняет "безопасный" метод (GET, HEAD, OPTIONS), разрешаем доступ
        if request.method in permissions.SAFE_METHODS:
            return True

        # Если метод запроса не является "безопасным", проверяем, является ли пользователь владельцем объекта
        return obj.user == request.user