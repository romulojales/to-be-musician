from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
import autoslug


class Artist(models.Model):
    api_id = models.CharField(_('API ID'), max_length=100, db_index=True)
    name = models.CharField(_('Name'), max_length=255)
    slug = autoslug.AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class Album(models.Model):
    api_id = models.CharField(_('API ID'), max_length=100, db_index=True)
    name = models.CharField(_('Name'), max_length=255)
    slug = autoslug.AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class Song(models.Model):
    api_id = models.CharField(_('API ID'), max_length=100, db_index=True)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    name = models.CharField(_('Name'), max_length=255)
    tinysong_url = models.URLField('Tinysong URL')
    slug = autoslug.AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class Interpretation(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)

    def __unicode__(self):
        return u"{0}'s interpretation of {1} ({2})".format(self.user.first_name,
                                                           self.song.name,
                                                           self.song.artist.name)
