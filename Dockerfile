FROM python:3.8.0-alpine

RUN apk update && \
    apk add \
        gcc \
        python3-dev

RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r /requirements.txt
