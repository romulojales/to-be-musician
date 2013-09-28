
from .test_utils import *
from .test_filter_song_flash_player import *


class RequestJson(object):
    code = 200

    def __init__(self, json):
        self.content = json

    def get(self, *args, **kwargs):
        return self.content

    def json(self):
        return self.content
