#!/usr/bin/env python3
from quart import request
from quart_trio import QuartTrio
import trio


app = QuartTrio(__name__)


@app.route("/endpoint/", methods=["POST"])
async def endpoint():
    request_json = await request.get_json()
    return {"May this connection": "never die!", "requested": request_json}
