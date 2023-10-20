from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .filters import DocumentFilter
from .models import Document, CustomUser
from .permissions import IsOwnerOrReadOnly
from .serializers import DocumentSerializer, UserSerializer

# Ниже приведены комментарии к каждому из представлений API

class UserRegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # Представление для регистрации пользователей. Мы используем CreateAPIView, задаем queryset и
    # сериализатор UserSerializer для создания новых пользователей.

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DocumentFilter
    # Это представление для работы с документами. Мы используем ModelViewSet, чтобы обеспечить стандартные CRUD-операции.
    # Здесь мы задаем queryset, сериализатор DocumentSerializer, парсер MultiPartParser для обработки файлов,
    # правила доступа IsOwnerOrReadOnly и фильтры DocumentFilter.

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        # Проверка, аутентифицирован ли пользователь. Если нет, возвращаем ошибку 401 Unauthorized.

        files = request.FILES
        data = request.data

        try:
            name = data.get('name')
            description = data.get('description')
            file = files.get('file')

            serializer = DocumentSerializer(data={'name': name, 'description': description, 'file': file})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"message": "Document created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        # Создание нового документа, прикрепление его к текущему пользователю и обработка ошибок.


