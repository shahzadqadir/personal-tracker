# get an image from dockerhub
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /code

# copy requirements files
COPY Pipfile Pipfile.lock /code/

# install pipenv and requirements
RUN pip install pipenv && pipenv install --system

# copy rest of project files
COPY . /code/