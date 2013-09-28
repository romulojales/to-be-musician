

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
