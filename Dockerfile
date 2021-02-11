FROM python:3.9-alpine
LABEL  MAINTAINER="jwyjohn <jwyjohn@foxmail.com>"

ENV LIBRARY_PATH /lib:/usr/lib

COPY ./app /app/

RUN cat /etc/apk/repositories | sed -e "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/" | tee /etc/apk/repositories && \
    apk add build-base python3-dev gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev libxslt-dev && \
    cd /app && pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt && \
    apk del build-base && rm -rf /var/cache/apk/*

VOLUME [ "/app/data" ]

WORKDIR /app

ENTRYPOINT [ "python", "/app/main.py" ]
