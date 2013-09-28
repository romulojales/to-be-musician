from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from songs.models import Song
from musician.models import Song as MusicianSong


class SongStateView(RedirectView):

    def get_redirect_url(self, **kwargs):
        song = get_object_or_404(Song, id=kwargs['id'])
        musician_song = self.set_song_state(song, kwargs['state'])
        return song.get_absolute_url()

    def set_song_state(self, song, state):
        return MusicianSong.objects.get_or_create(song=song, state=state,
                                                  user=self.request.user)
