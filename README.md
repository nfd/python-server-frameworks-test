What is this?
===
This is a benchmark to demonstrate a real-world test case in which the ASGI server framework I was using timed out. With
this repo you can benchmark various different server + web framework combinations.

Running tests
===

    docker-compose up

Enter the server container and run the shell script of the server of interest. For example:

    docker-compose exec server bash
	./server-django-requests-daphne-asgi.sh

In another window, run the client:

    docker-compose exec client python3 /app/client.py


