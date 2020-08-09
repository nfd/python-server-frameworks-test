import threading
import time
import random

import requests

THREADS = 30
ENDPOINT = "http://server:8000/endpoint/"
TIMEOUT = 10
PAYLOAD = {"An example of": "A POSTed JSON payload"}

successful = 0

def _post_one(session, delay=0):
    try:
        result = session.post(ENDPOINT, json=PAYLOAD, timeout=TIMEOUT)
        if result.status_code != 200:
            return f'Status {result.status_code}'

        if delay:
            time.sleep(delay)

        result_json = result.json()

        if result_json["requested"] != PAYLOAD:
            return 'Bad JSON'

    except requests.exceptions.Timeout:
        return 'Timeout'


def _retry_until_fail():
    global successful
    while True:
        with requests.Session() as session:
            if result := _post_one(session):
                print(result)
                return

            if result := _post_one(session, 1 + random.random()):
                print(result)
                return
        # No mutex because lol GIL
        successful += 1
        if successful % 100 == 0:
            print(f"Successful requests: {successful}")


def _client():
    while True:
        _retry_until_fail()


def demo():
    for _ in range(THREADS):
        thread = threading.Thread(target=_client, daemon=True)
        thread.start()

    print("Press enter to stop.")
    input()


if __name__ == '__main__':
    demo()
