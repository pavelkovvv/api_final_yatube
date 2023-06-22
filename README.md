# REST API Yatube

## Описание проекта

API для [проекта социальной сети Yatube](https://github.com/pavelkovvv/yatube). 

В проекте реализованы следующие функции:

- REST API
- Сортировка, фильтрация и поиск по запросу
- Пагинация ответов (по необходимости)
- Для аутентификации применяются JWT - токены

## Системные требования

- Python 3.9+
- Linux, Windows, MacOS, BSD

## Технологии

- Python 3.9
- Django 3.2.16
- Django REST Framework
- SQLite3

## Установка проекта и его запуск

1. Клонировать репозиторий и перейти в него:
```
git clone git@github.com:pavelkovvv/api_final_yatube.git
```

2. Создать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

3. Обновить pip и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:
```
python manage.py migrate
```

5. Запустить проект:
```
python manage.py runserver
```


## Примеры запросов к API
Request (получение всех публикаций):

<span style="color:green;font-weight:700;font-size:20px">
    GET
</span>
<span style="font-weight:700;font-size:16px">
    /api/v1/posts/
</span>

Response:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Request (Создание публикации):

<span style="color:blue;font-weight:700;font-size:20px">
    GET
</span>
<span style="font-weight:700;font-size:16px">
    /api/v1/posts/
</span>

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Response:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

Request (Получение конкретной публикации):

<span style="color:blue;font-weight:700;font-size:20px">
    GET
</span>
<span style="font-weight:700;font-size:16px">
    /api/v1/posts/{id}/
</span>

Response:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

Request (Обновление публикации):

<span style="color:purple;font-weight:700;font-size:20px">
    PUT
</span>
<span style="font-weight:700;font-size:16px">
    /api/v1/posts/{id}/
</span>

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Response:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

Request (Частичное обновление публикации):

<span style="color:darkorange;font-weight:700;font-size:20px">
    PATCH
</span>
<span style="font-weight:700;font-size:16px">
    /api/v1/posts/{id}/
</span>

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Response:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

Request (Удаление публикации):

<span style="color:red;font-weight:700;font-size:20px">
    DELETE
</span>
<span style="font-weight:700;font-size:16px">
    /api/v1/posts/{id}/
</span>

Response:
```
{
  "detail": "Учетные данные не были предоставлены."
}
```

## Документация к проекту

Документация для API доступна по адресу ```/redoc/``` 
(только после запуска проекта).
