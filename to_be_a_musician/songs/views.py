from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView
from songs.forms import InterpretationForm
from songs.models import Interpretation, Song


class SongView(DetailView):
    model = Song

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        artist_slug = self.kwargs['artist_slug']
        song_slug = self.kwargs['song_slug']

        return get_object_or_404(queryset, slug=song_slug,
                                 artist__slug=artist_slug)

    def get_context_data(self, *args, **kwargs):
        context = super(SongView, self).get_context_data(**kwargs)
        context["request"] = self.request
        return context


class InterpretationCreateView(CreateView):
    model = Interpretation
    form_class = InterpretationForm

    def get_context_data(self, *args, **kwargs):
        context = super(InterpretationCreateView, self).get_context_data(**kwargs)
        context['song'] = self.get_song_object()

        return context

    def form_valid(self, form):
        song = self.get_song_object()
        self.object = form.save(user=self.request.user, song=song)
        return HttpResponseRedirect(song.get_absolute_url())

    def get_song_object(self):
        artist_slug = self.kwargs['artist_slug']
        song_slug = self.kwargs['song_slug']
        song = get_object_or_404(Song, slug=song_slug,
                                 artist__slug=artist_slug)
        return song
