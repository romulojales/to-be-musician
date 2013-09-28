from django.http.response import HttpResponse
from django.utils import simplejson

from .models import search_songs


def search(request, params):
    musics = search_songs(params)
    json = []
    for music in musics:
        json.append({"name": music.songName,
                     "artist": music.artistName,
                     "url": music.get_absolute_url()})
    return HttpResponse(simplejson.dumps(json), mimetype="application/json")


def song(requests, songId):
    pass
