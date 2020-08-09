
#!/bin/bash

cd /app/django-requests/mysite
hypercorn --bind 0.0.0.0:8000 mysite.asgi:application
