FROM python:3.9-slim-buster

RUN mkdir /app
ENV PYTHONPATH=/app
WORKDIR /app
COPY requirements.txt .
RUN pip install --proxy=http://185.240.151.154:8080 -r requirements.txt
ADD . .

RUN pip install --proxy=http://185.240.151.154:8080 -e .

ENTRYPOINT ./runserver.sh
