# Сайт риэлторского агентства

Сайт представляет собой базу данных квартир. На главной странице показываются 
актуальные квартиры, также есть фильтр по городу, новостройкам и стоимости.

Квартиры заносятся и изменяются через админку сайта, доступную по адресу 
[127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/).


## Запуск

- Скачайте код
- Установите зависимости командой 
```sh
pip install -r requirements.txt
```
- Создайте файл базы данных и сразу примените все миграции командой 
```sh
python3 manage.py 
```
- Запустите сервер командой 
```sh
python3 manage.py runserver
```

Для входа в админку необходимо создать администратора сайта 
(суперпользователя) командой:
```sh
python manage.py createsuperuser
```
После создания администратора зайдите в админку с указанными ранее данными.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

    Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
