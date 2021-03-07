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
Корневая точка http://localhost:8000/api/system/

Админка http://localhost:8000/admin/

Конечная точка для генерации JWT токена http://localhost:8000/api/token/
#
Шаблон JSON Post запроса:

```
{"person": {
    "title": "somebody",
    "age": 42,
    "address": "something"
    }
}
```

