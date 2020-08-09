#!/bin/bash

cd /app/flask-requests
gunicorn -b 0.0.0.0:8000 --threads 10 server:app
