FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt upgrade -y

RUN apt install python-dev -y
RUN apt install python3-dev -y
RUN apt install libpq-dev -y

RUN mkdir /app
WORKDIR /app

Add requirements.txt /app

RUN pip3 install -r requirements.txt

ADD . /app
