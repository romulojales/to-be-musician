from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from songs.models import Song


class Song(models.Model):
    SONG_STATES = (
        ('learn', _('will learn')),
        ('learning', _('is learning')),
        ('learned', _('has learned')),
    )

    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    state = models.CharField(_('State'), choices=SONG_STATES, max_length=25,
                             default='learn')

    class Meta:
        unique_together = ('user', 'song', )

    def __unicode__(self):
        return "{0} {1} {2}".format(self.user.username, self.get_state_display(),
                                    self.song)
