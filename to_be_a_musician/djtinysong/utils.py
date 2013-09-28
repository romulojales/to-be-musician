import logging
from django.conf import settings
import requests

API_TINYSONG_URL = u"http://tinysong.com/s/{ARG}"


def search_music(argument, page=1, limit=32):
    offset = limit * (page - 1)
    musics = get(argument, {"offset": offset, "limit": limit})
    return musics


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
