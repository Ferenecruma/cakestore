# set official base image
FROM python:3.8.6-slim

# set work directory
WORKDIR /cakestore

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /cakestore/

RUN python manage.py migrate
