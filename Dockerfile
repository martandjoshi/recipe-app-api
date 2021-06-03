FROM python:3.9.5-alpine3.13

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client 
RUN apk add --update --no-cache --virtual .tmp_build_dep \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp_build_dep

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user