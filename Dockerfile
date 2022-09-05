# pull official base image
FROM python:latest

# set work directory
WORKDIR /usr/apps/apis/ocr
COPY . /usr/apps/apis/ocr/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apk add tessaract-ocr
RUN apt update && apt install tesseract-ocr -y \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r  requirements.txt 

