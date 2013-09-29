from django.template import Library
from musician.models import Song

register = Library()


@register.inclusion_tag('templatetags/learn_button.html')
def learn_button(user, song):
    if not user:
        return {'song': song, 'state': None}

    try:
        musician_song = Song.objects.get(user=user, song=song)
        state = musician_song.state
    except Song.DoesNotExist:
        state = None

    return {'song': song, 'state': state}
