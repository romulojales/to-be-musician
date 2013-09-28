from django.conf import settings

API_TINYSONG_URL = "http://tinysong.com/s/{ARG}"
#
SONG_URL = getattr(settings, "TINYSONG_SONG_URL", "song/(?P<songId>[\d]+)")
