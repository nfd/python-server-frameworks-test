import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def endpoint(request, methods=["POST"]):
    json_request = json.loads(request.body)

    return JsonResponse({"Example response": "Is here", "requested": json_request})
