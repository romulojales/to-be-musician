import requests
from djtinysong import API_TINYSONG_URL


def get(argument, params):
    url = API_TINYSONG_URL.format(ARG=argument)
    return requests.get(url, params=params).json()
