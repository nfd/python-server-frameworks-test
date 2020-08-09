#!/bin/bash

cd /app/django-requests/mysite
gunicorn -b 0.0.0.0:8000 --threads 10 mysite.wsgi:application
