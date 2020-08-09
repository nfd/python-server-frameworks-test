
#!/bin/bash

cd /app/quart-requests
daphne -b 0.0.0.0 server:app
