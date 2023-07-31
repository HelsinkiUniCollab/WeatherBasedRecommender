FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock*  /app/

RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    wget \
    git \
    curl \
    libaec-dev \
    gfortran

COPY install_eccodes.sh /app/
RUN chmod +x /app/install_eccodes.sh && /app/install_eccodes.sh

RUN poetry run pip install eccodes
RUN poetry run pip install netCDF4

COPY . /app

ENV FLASK_APP=src/app:app
ENV REQUEST_ORIGIN=http://localhost:3000

EXPOSE 5000

CMD ["poetry", "run", "gunicorn", "-b", ":5000", "--timeout", "300", "-w", "4", "src.app:app"]
