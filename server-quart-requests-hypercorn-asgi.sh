
#!/bin/bash

cd /app/quart-requests
hypercorn --bind 0.0.0.0:8000 -k asyncio server:app
