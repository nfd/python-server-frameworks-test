#!/usr/bin/env python3
from quart import Quart, request


app = Quart(__name__)


@app.route("/endpoint/", methods=["POST"])
async def endpoint():
    request_json = await request.get_json()
    return {"May this connection": "never die!", "requested": request_json}
