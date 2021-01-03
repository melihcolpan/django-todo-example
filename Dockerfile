FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /todo_project
WORKDIR /todo_project
ADD . /todo_project/

RUN pip install -r requirements.txt
