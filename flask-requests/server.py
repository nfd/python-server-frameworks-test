#!/usr/bin/env python3
from flask import Flask, request


app = Flask(__name__)


@app.route("/endpoint/", methods=["POST"])
def endpoint():
    request_json = request.get_json()
    return {"May this connection": "never die!", "requested": request_json}
