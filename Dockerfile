FROM python:3.8.3-buster

# Use pip to update itself.
RUN python3 -m pip install -U pip

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000
