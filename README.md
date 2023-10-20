# docs

1. Клонируйте репозиторий с проектом.
   git clone https://github.com/yourusername/yourproject.git

2. Перейдите в каталог проекта
   cd yourproject/

3. Создайте вирутуальное окружение и активируйте его
python -m venv venv
source venv/bin/activate  

4. Установите зависимости из файла requirements.txt
  pip install -r requirements.txt

5. Запуск сервера:
   Примените миграции:
      python manage.py migrate
   Запустите сервер разработки:
     python manage.py runserver
   
Откройте ваш веб-браузер и перейдите по адресу http://localhost:8000/ для доступа к проекту.


# Работа с API: (При получении документа, вставьте ссылку на него в браузер, так вы можете увидеть его полностью)

1. Аутентификация
Для работы с API необходима аутентификация. Вы можете использовать JWT-токены для аутентификации. Для получения токена отправьте POST-запрос на /api/token/ с параметрами username и password. Токен будет возвращен в ответе.

2. Регистрация пользователя
Чтобы зарегистрировать нового пользователя, отправьте POST-запрос на /api/register/ с параметрами email и password. Пользователь будет создан, и вы получите подтверждение.

3. Работа с документами
API позволяет вам работать с документами. Вы можете выполнять следующие действия:
   1) Получить список всех документов: GET /api/document/
   2) Создать новый документ: POST /api/document/
   3) Получить информацию о конкретном документе: GET /api/document/{id}/
   4) Обновить информацию о документе: PUT /api/document/{id}/
   5) Удалить документ: DELETE /api/document/{id}/
   6) Для создания нового документа, отправьте POST-запрос на /api/document/ с параметрами name, description и file. Пользователь должен быть аутентифицирован.

Для получения информации о документе, обновления или удаления, отправьте соответствующие запросы с указанием идентификатора документа.

4. Фильтрация документов
   API поддерживает фильтрацию документов по различным параметрам. Вы можете использовать запросы, поддерживаемые фильтры, чтобы получить только нужные документы.

   Пример запроса для фильтрации по названию документа:

   GET /api/document/?name=Название_документа

5. Административная панель
   Вы можете войти в административную панель Django, используя учетные данные суперпользователя, созданные ранее. Административная панель доступна по адресу /admin/ и позволяет управлять пользователями и документами.






