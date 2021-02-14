FROM python:3.9-alpine
LABEL  MAINTAINER="jwyjohn <jwyjohn@foxmail.com>"

ENV LIBRARY_PATH /lib:/usr/lib


RUN cat /etc/apk/repositories | sed -e "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/" | tee /etc/apk/repositories && \
    apk add build-base python3-dev gcc musl-dev zlib-dev

COPY ./requirements.txt /app/requirements.txt

RUN cd /app && pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt && \
    apk del build-base && rm -rf /var/cache/apk/*

# VOLUME [ "/data","/app" ]

# COPY ./app/ /app/

WORKDIR /app

# ENTRYPOINT [ "python", "/app/api.py" ]

ENTRYPOINT [ "gunicorn", "api:app", "-c", "/app/gunicorn.conf" ]
