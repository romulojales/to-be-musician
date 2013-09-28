from djtinysong import utils
from django.core.urlresolvers import reverse


class Song(object):

    def __init__(self, *args, **kwargs):
        if "SongID" in kwargs:
            self.songId = kwargs["SongID"]
        if "SongName" in kwargs:
            self.songName = kwargs["SongName"]
        if "ArtistID" in kwargs:
            self.artistId = kwargs["ArtistID"]
        if "ArtistName" in kwargs:
            self.artistName = kwargs["ArtistName"]
        if "AlbumID" in kwargs:
            self.albumId = kwargs["AlbumID"]
        if "AlbumName" in kwargs:
            self.albumName = kwargs["AlbumName"]
        if "Url" in kwargs:
            self.tinySongURL = kwargs["Url"]

    def get_absolute_url(self):
        url = reverse("tinysong_song", args=(self.songId,))
        return url

    def player(self):
        return '''<embed src="http://grooveshark.com/songWidget.swf" 
        type="application/x-shockwave-flash" 
        width="250" 
        height="40" 
        flashvars="hostname=cowbell.grooveshark.com&amp;songIDs=%s&amp;style=metal&amp;p=0"
        allowscriptaccess="always"
        wmode="window">''' % self.songId


def search_songs(argument, limit=32, page=1):
    offset = limit * (page - 1)
    musics = utils.get(argument, {"offset": offset, "limit": limit})
    musics = [Song(**song) for song in musics]
    return musics
