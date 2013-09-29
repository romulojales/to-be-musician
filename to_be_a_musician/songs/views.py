from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from songs.forms import InterpretationForm
from songs.models import Interpretation, Song


class SongsGetSongObjectMixin(object):

    def get_song_object(self):
        artist_slug = self.kwargs['artist_slug']
        song_slug = self.kwargs['song_slug']
        song = get_object_or_404(Song, slug=song_slug,
                                 artist__slug=artist_slug)
        return song


class SongsGetObjectMixin(object):

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        kwargs = self.get_queryset_kwargs()
        return get_object_or_404(queryset, **kwargs)

    def get_queryset_kwargs(self):
        kwargs = {
            'song__artist__slug': self.kwargs['artist_slug'],
            'song__slug': self.kwargs['song_slug'],
            'id': self.kwargs['id'],
        }
        return kwargs


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


class InterpretationCreateView(SongsGetSongObjectMixin, CreateView):
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


class InterpretationUpdateView(SongsGetSongObjectMixin, SongsGetObjectMixin, UpdateView):
    model = Interpretation
    form_class = InterpretationForm

    def get_context_data(self, *args, **kwargs):
        context = super(InterpretationUpdateView, self).get_context_data(**kwargs)
        context['song'] = self.get_song_object()

        return context

    def get_queryset_kwargs(self):
        kwargs = super(InterpretationUpdateView, self).get_queryset_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def form_valid(self, form):
        song = self.get_song_object()
        self.object = form.save(user=self.request.user, song=song)
        return HttpResponseRedirect(self.object.get_absolute_url())


class InterpretationView(SongsGetObjectMixin, DetailView):
    model = Interpretation
