FROM python:3.8.10-alpine3.13

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # python dependencies
  && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
  # msyql dependencies
  && apk add mariadb-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev libjpeg 

# Requirements are installed here to ensure they will be cached.
COPY requirements/*.txt /requirements/
RUN pip install -r /requirements/local.txt

RUN apk del build-deps

WORKDIR /app