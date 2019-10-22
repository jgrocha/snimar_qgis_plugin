FROM ubuntu:18.04

RUN apt update && apt upgrade -y

RUN apt install -y python3-pyqt5 pyqt5-dev-tools make zip

WORKDIR /code

COPY . .
