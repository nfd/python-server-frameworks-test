
#!/bin/bash

cd /app/quart-requests
uvicorn --host 0.0.0.0 server:app
