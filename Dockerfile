FROM python:3.11
RUN apt install libpq-dev
COPY requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
COPY . /code
WORKDIR /code