FROM ubuntu:18.04

RUN apt-get update

RUN mkdir /app
WORKDIR /app

ADD . /app

RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
