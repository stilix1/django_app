# Django Steam Games Parser

Это веб-приложение на Django, созданное для парсинга данных игр Steam и их хранения в базе данных. Проект был разработан для изучения Django, работы с внешними API и настройки деплоя с использованием Docker. Он включает базовую функциональность для управления данными через веб-интерфейс или REST API.

## Функциональность
- Парсинг данных игр Steam с использованием AJAX.
- Хранение данных в базе данных (SQLite/PostgreSQL).
- Отображение данных через веб-интерфейс.
- Контейнеризация с использованием Docker и Docker Compose для упрощения деплоя.

## Технологии
- **Python 3.x** — язык программирования.
- **Django 4.x** — фреймворк для веб-разработки.
- **Django REST Framework** — библиотека для создания API (если используется).
- **JavaScript** — для клиентской логики (AJAX).
- **HTML/CSS** — для фронтенд-интерфейса.
- **SQLite/PostgreSQL** — база данных.
- **Docker** — контейнеризация.
- **Docker Compose** — оркестрация контейнеров.
- **Gunicorn** — WSGI-сервер для продакшн-деплоя.
- **Git** — контроль версий.

## Установка
### Локальный запуск
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/stilix1/django_app.git

    Перейдите в директорию проекта:
    bash

cd django_app
Создайте виртуальное окружение и активируйте его:
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Установите зависимости:
bash
pip install -r requirements.txt
Настройте базу данных в settings.py или создайте .env файл:
env
DATABASE_URL=sqlite:///db.sqlite3
(Или укажите настройки для PostgreSQL.)
Выполните миграции:
bash
python manage.py migrate
Запустите сервер:
bash

    python manage.py runserver
    Откройте приложение в браузере: http://localhost:8000.

Запуск через Docker

    Убедитесь, что Docker и Docker Compose установлены:
    bash

docker --version
docker-compose --version
Запустите приложение:
bash

    docker-compose up --build
    Откройте приложение: http://localhost:8000.

Использование

    Перейдите на главную страницу для просмотра парсированных данных Steam через веб-интерфейс.
    Если настроен API, отправьте запросы, например:
    bash

    curl http://localhost:8000/api/games/

О проекте

Этот проект был создан для изучения Django и экспериментов с парсингом данных. Он демонстрирует:

    Работу с Django для серверной разработки.
    Интеграцию с внешними API (Steam) через AJAX.
    Настройку деплоя с использованием Docker и Gunicorn.
    Использование Git для управления кодом.
