# Используем официальный slim-образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения в контейнер
COPY . .

# Определяем переменные окружения
ENV SECRET_KEY="9d741676ff72d4af76edda2d3d11e11f35d76b05a1e5f5fb5adec5871d7821c95c4ee89b4eb2757f6838fc36341c72173daf"
ENV CELERY_BROKER_URL="redis://redis:6379/0"
ENV CELERY_BACKEND="redis://redis:6379/0"

# Создаем директорию для медиафайлов
RUN mkdir -p /app/media

EXPOSE 8000
CMD ["python","manage.py", "runserver","0.0.0.0:8000"]