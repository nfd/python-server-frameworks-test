
#!/bin/bash

cd /app/django-requests/mysite
uvicorn --host 0.0.0.0 mysite.asgi:application
