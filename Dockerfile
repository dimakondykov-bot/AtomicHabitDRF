# Указываем базовый образ
FROM python:3.12-slim

# Запрещаем Python копить мусорные файлы кэша .pyc в контейнере
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
# Запускаем Gunicorn вместо учебного runserver.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
