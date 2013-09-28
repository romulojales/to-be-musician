import logging

from django.conf import settings

from djtinysong import API_TINYSONG_URL
import requests


def get(argument, params):
    url = API_TINYSONG_URL.format(ARG=argument)
    params["format"] = 'json'
    if "key" not in params:
        params["key"] = settings.TINYSONG_KEY
    json = []
    try:
        response = requests.get(url, params=params)
        json = response.json()
    except:
        logging.exception("an error occured when dealing with tinysong")
    finally:
        return json
