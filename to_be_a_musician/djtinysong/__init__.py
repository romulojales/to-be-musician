from django.conf import settings

API_TINYSONG_URL = "http://tinysong.com/s/{PARAMS}?format=json&key=%s" % \
                                                        settings.TINYSONG_KEY
#
SONG_URL = getattr(settings, "TINYSONG_SONG_URL", "song/\d+")
