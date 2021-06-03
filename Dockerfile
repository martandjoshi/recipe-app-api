FROM python:3.9.5-alpine3.13

ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client 
RUN apk add --update --no-cache --virtual .tmp_build_dep \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
<<<<<<< HEAD
RUN apk del .tmp_build_dep
=======
RUN apk del .tmp-build-deps
>>>>>>> c55c99a6415f115ed8f7c75dedb39009066313db

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user