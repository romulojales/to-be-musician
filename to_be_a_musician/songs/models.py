from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import autoslug
from djtinysong import search_music


class Artist(models.Model):
    api_id = models.CharField(_('API ID'), max_length=100, blank=True,
                              null=True, db_index=True)
    name = models.CharField(_('Name'), max_length=255)
    slug = autoslug.AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class Album(models.Model):
    api_id = models.CharField(_('API ID'), max_length=100, blank=True,
                              null=True, db_index=True)
    name = models.CharField(_('Name'), max_length=255)
    slug = autoslug.AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class Song(models.Model):
    api_id = models.CharField(_('API ID'), max_length=100, blank=True,
                              null=True, db_index=True)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    name = models.CharField(_('Name'), max_length=255)
    tinysong_url = models.URLField('Tinysong URL')
    slug = autoslug.AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('songs_song', kwargs={
            'artist_slug': self.artist.slug,
            'song_slug': self.slug,
        })

    def last_interpretations(self):
        return self.interpretation_set.order_by('-created_at')[:10]


class Interpretation(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    created_at = models.DateTimeField(_('Created at'), default=timezone.now)
    last_update = models.DateTimeField(_('Last update'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    youtube_url = models.URLField(_('Youtube URL'), blank=True, null=True)
    songsterr_url = models.URLField(_('Songsterr URL'), blank=True, null=True)
    soundcloud_url = models.URLField(_('Soundcloud URL'), blank=True, null=True)

    def __unicode__(self):
        return u"{0}'s interpretation of {1} ({2})".format(self.user.username,
                                                           self.song.name,
                                                           self.song.artist.name)

    def get_absolute_url(self):
        return reverse('songs_interpretation_detail', kwargs={
            'artist_slug': self.song.artist.slug,
            'song_slug': self.song.slug,
            'id': self.pk,
        })

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        return super(Interpretation, self).save(*args, **kwargs)


def search_songs(argument, page=1):
    musics = search_music(argument, page=page)
    songs = []
    for music in musics:
        artist, created = Artist.objects.get_or_create(api_id=music["ArtistID"],
                                                       name=music["ArtistName"])
        if created:
            artist.save()
        album, created = Album.objects.get_or_create(api_id=music["AlbumID"],
                                                     name=music["AlbumName"])
        if created:
            album.save()
        song, created = Song.objects.get_or_create(api_id=music["SongID"],
                                                   artist=artist,
                                                   album=album,
                                                   name=music["SongName"],
                                                   tinysong_url=music["Url"])
        if created:
            song.save()
        songs.append(song)
    return songs
