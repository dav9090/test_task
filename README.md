REST API для справочника организаций, зданий и видов деятельности.

## Описание
Данный тестовый проект выполнен для "Secunda".
Дряхловым Александром https://hh.ru/resume/eeb58586ff0e1a1f940039ed1f785571663236

## 📦 Технологии
- FastAPI
- SQLAlchemy
- Alembic
- Docker

## 🚀 Запуск
🚀 Запуск проекта (3 способа)
✅ 1. Через Docker (рекомендуется)
Если установлен Docker:

docker-compose up --build
Откроется FastAPI по адресу: http://localhost:8000/docs

✅ 2. Без Docker — вручную
Если ты работаешь локально с Python + venv:

Шаг 1. Активируй виртуальное окружение
.\.venv\Scripts\activate

Шаг 2. Установи зависимости
pip install -r requirements.txt

Шаг 3. Прогони Alembic
alembic upgrade head

Шаг 4. Заполни базу тестовыми данными
python seed_data.py

Шаг 5. Запусти FastAPI
uvicorn main:app --reload
Теперь API доступно на:
📍 http://localhost:8000/docs

✅ 3. Через IDE (например PyCharm)
Открой проект.
Убедись, что .venv активирован.
Установи зависимости (requirements.txt).
Запусти main.py — FastAPI сервер стартует.


Приложение будет доступно по адресу: [http://localhost:8000/docs](http://localhost:8000/docs)
API_KEY=supersecretkey777


### Структура
- `main.py` — точка входа
- `routers/` — обработчики маршрутов
- `models.py` — SQLAlchemy модели
- `schemas.py` — Pydantic-схемы
- `db.py` — подключение к БД
- `utils.py`, `dependencies.py` — вспомогательные утилиты

## 📌 API Функционал
- Поиск организаций по названию, координатам, зданию, виду деятельности
- Поддержка дерева до 3 уровней
- Swagger-документация автоматически доступна по `/docs`

p.s. На проде файл .env будет в .gitignore и в репозитории его не будет
