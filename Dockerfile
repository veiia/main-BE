FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /main
WORKDIR /main

COPY requirements requirements

RUN python -m pip install --upgrade pip
RUN pip3 install -r /main/requirements/base.txt

COPY . .
