# rest-api-djangо

Для запуска проекта на вашей машине должен быть предустановлен Python версии 3.6+.

# Getting started

(находясь в директории rest-api-django, используя терминал в PyCharm или командную строку)
1. Выполните команду:

    `pip install -r requirements.txt`
  
2. Выполните миграции:

    `python manage.py makemigrations`
    
    `python manage.py migrate`
  
3. Создайте суперпользователя(админа), заполнив несколько полей:

    `python manage.py createsuperuser`
 
 
4. Запустите локальный сервер (по умолчанию на 8000 порту):

    `python manage.py runserver`
    
#
Регистрация пользователя, просмотр всех пользователей http://localhost:8000/auth/users/

Текущий пользователь http://localhost:8000/auth/users/me/

Генерация JWT токена http://localhost:8000/auth/jwt/create/

Рефреш токена http://localhost:8000/auth/jwt/refresh/

Админка http://localhost:8000/admin/

Все сборы данного юзера http://localhost:8000/api/system/

Определенный сбор и информация по нему http://localhost:8000/api/system/<pk>



