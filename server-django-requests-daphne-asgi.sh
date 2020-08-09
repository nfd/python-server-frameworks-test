#!/bin/bash

cd /app/django-requests/mysite
daphne -b 0.0.0.0 mysite.asgi:application
