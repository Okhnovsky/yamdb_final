![workflow](https://github.com/Okhnovsky/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)
### YaMDb - отзывы на произведения.
### О проекте
YaMDb позволяет пользователям оставлять отзывы к различного рода
произведениям: музыке, фильмам, книгам.

Однако сами произведения в YaMDb отсутствуют.

## Действующий IP адрес:
```bash
158.160.58.167 
```

## Шаблон наполнения .env:
- Создайте файл .env
- Добавьте в .env следующее:

```bash
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```

## Запуск проекта
- Клонируйте репозиторий.
- Перейдите в директорию ```infra``` и запустите приложение в контейнерах:

```bash
docker-compose up -d --build
```

- Затем выполните миграции, создайте суперпользователя и соберите статику:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

- Заполните базу данных:

```bash
docker-compose exec web python manage.py loaddata ../infra/fixtures.json
```

## Документация и примеры использования API:
Доступны по GET-запросу на эндпойнт /redoc/

Автор проекта:
- [Александр Охновский](https://github.com/Okhnovsky)
