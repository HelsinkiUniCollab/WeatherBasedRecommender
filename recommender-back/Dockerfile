FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock*  /app/

RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

RUN apt-get update && apt-get install -y \
    libeccodes0 \
    libeccodes-dev \
    libeccodes-tools

RUN poetry run pip install --upgrade eccodes

COPY . /app

ENV FLASK_APP=src/app:app
ENV REQUEST_ORIGIN=http://localhost:3000

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
