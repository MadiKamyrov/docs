import django_filters  # Импортируем модуль django_filters для создания фильтров


# Создаем фильтр для модели Document
class DocumentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # В этом фильтре мы используем CharFilter для поля "name" и указываем lookup_expr 'icontains',
    # что означает, что фильтрация будет происходить с игнорированием регистра (icontains).
