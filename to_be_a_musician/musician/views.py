from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView

from musician.models import Song as MusicianSong
from songs.models import Song


class SongStateView(RedirectView):

    def get_redirect_url(self, **kwargs):
        song = get_object_or_404(Song, id=kwargs['id'])
        self.set_song_state(song, kwargs['state'])

        return song.get_absolute_url()

    def set_song_state(self, song, state):
        musician_song = MusicianSong.objects.get_or_create(song=song, user=self.request.user)[0]

        musician_song.state = state
        musician_song.save()

    def get_context_data(self, *arg, **kwargs):
        context = super(SongStateView, self).get_context_data(**kwargs)
        context["request"] = self.request
        return context


class MusicianView(DetailView):
    model = User
    template_name = "musician.html"

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['user_name'])

    def get_context_data(self, *arg, **kwargs):
        context = super(MusicianView, self).get_context_data(**kwargs)
        context["will_learn"] = self.object.song_set.filter(state="learn")
        context["learning"] = self.object.song_set.filter(state="learning")
        context["has_learned"] = self.object.song_set.filter(state="learned")
        context["request"] = self.request
        return context
