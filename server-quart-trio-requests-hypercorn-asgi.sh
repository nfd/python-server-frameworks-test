
#!/bin/bash

cd /app/quart-trio-requests
hypercorn --bind 0.0.0.0:8000 -k trio server:app
