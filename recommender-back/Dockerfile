FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY pyproject.toml poetry.lock*  /app/

RUN pip install poetry \
  && pip install flask \
  && poetry config \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . /app

ENV FLASK_APP=api:api

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
