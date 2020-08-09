All tests are ASGI unless noted.

Versions

 * daphne 2.5.0
 * django 3.1
 * flask 1.1.2
 * gunicorn 20.0.4
 * hypercorn 0.10.2
 * quart 0.13.0
 * quart-trio 0.5.1
 * trio 0.16.0
 * uvicorn 0.11.8

Successful 

 * django + gunicorn (wsgi)
 * django + daphne
 * django + hypercorn
 * django + uvicorn
 * flask + gunicorn (wsgi)
 * quart + hypercorn (also extended stress test)
 * quart + daphne

Unsuccessful

 * quart-trio + hypercorn (frequent timeouts)
 * quart + uvicorn (frequent timeouts)


