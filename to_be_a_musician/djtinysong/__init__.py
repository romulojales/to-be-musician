from django.conf import settings

TINYSONG_URL = "http://tinysong.com/s/{PARAMS}?format=json&key=%s" % \
                                                        settings.TINYSONG_KEY
#
