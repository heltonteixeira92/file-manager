FROM python:3.11-slim-buster

# set environment variables
ENV PYTHONUNBUFFERED=1

WORKDIR /api

RUN apt update -y \
    && apt install -y --no-install-recommends \
    build-essential \
    libssl-dev libpq-dev \
    wait-for-it \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install -U pip &&\
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN cp contrib/env-sample .env

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]