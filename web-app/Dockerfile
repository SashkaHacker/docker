FROM python:3.12-slim

RUN mkdir /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app

ENV DATABASE_URL="//user:password@localhost:5432/database"

CMD ["python3", "main.py"]