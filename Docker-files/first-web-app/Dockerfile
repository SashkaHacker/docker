FROM python:3.12-slim

RUN mkdir /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python3", "main.py" ]
