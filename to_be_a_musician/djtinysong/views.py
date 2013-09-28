from django.http.response import HttpResponse
from djtinysong import TINYSONG_URL
import requests


def search(request, params):
    url = TINYSONG_URL.format(PARAMS=params)
    response = requests.get(url)
    return HttpResponse(response.json(), mimetype="application/json")
