from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    name = models.CharField(_('Name'), max_length=255)
    tinysong_url = models.URLField('Tinysong URL')

    def __unicode__(self):
        return self.name


class Interpretation(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)

    def __unicode__(self):
        return u"{0}'s interpretation of {1} ({2})".format(self.user.first_name,
                                                           self.song.name,
                                                           self.song.artist.name)
