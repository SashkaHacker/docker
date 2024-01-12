FROM python:3.12-slim as builder

RUN mkdir /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install numpy

FROM python:3.12-slim as runner

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/. .

EXPOSE 8000

CMD ["python3", "main.py"]