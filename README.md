Дипломный проект создания backend-часть для сайта объявлений. В проекте риализовано API с помощью Django REST Framework.
Стэк используемых технологий:
- Python 3.7+
- Jdoser 2.1.0
- Django 4.2.2
- DRF 3.14.0
- Requests 2.31.0
- Stripe 5.5.0
- Faker 19.2.0
- PostgreSQL
- Celery 5.3.1
- Redis 5.0.0
- Pillow 2.31.0

  С остальными зависимостями, которые используются в проекте можно ознакомиться командой:
```
cat requirements.txt
```
#### Вся документация доступна в Swagger и Redoс:

```
http://localhost:8000 /redoc/ или /swagger/
```


1. #### Клонируем репозиторий себе, либо скачиваем zip файл и распаковываем себе на локальную машину

2. переходим в папку skymarket командой:

```
cd skymarket
```

3. #### Создаем виртуальное окружение.

4. #### Устанавливаем зависимости командой:
```
pip install -r requirements.txt
```
5.  #### Для работы нам понадобится установить и настройть базу данных PostgreSQL 

6. #### Выполняем миграцию командой:

```
python manage.py migrate
```

7. #### Загрузка данных

- Загружаем тестовые данные командой:

```
python manage.py loaddata fixtures/users.json fixtures/ad.json fixtures/comments.json
```

8. #### Запустить сервер командой:

```
python manage.py runserver 8000
```
Для монтирования образа проекта и запуска  в docker используем команду:
```
docker-compose up --build
```

