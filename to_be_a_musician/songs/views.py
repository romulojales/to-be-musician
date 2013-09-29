from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView
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

    def get_context_data(self, *args, **kwargs):
        artist_slug = self.kwargs['artist_slug']
        song_slug = self.kwargs['song_slug']
        song = get_object_or_404(Song, slug=song_slug,
                                 artist__slug=artist_slug)

        context = super(InterpretationCreateView, self).get_context_data(**kwargs)
        context['song'] = song

        return context
