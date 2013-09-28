from django.views.generic.base import TemplateView
from djtinysong.models import Song


class SearchView(TemplateView):
    template_name = 'common/search.html'

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        songs = []

        if q:
            # TODO: Yes, we are mocking all this guys
            songs = [
                Song(SongID='1', SongName='Hit The Lights', ArtistID='1',
                     ArtistName='Metallica', AlbumID='1', AlbumName="Kill 'em All",
                     Url='http://tinysong.com/#/share/hit the lights/14463747'),
                Song(SongID='2', SongName='The Four Horsemen', ArtistID='1',
                     ArtistName='Metallica', AlbumID='1', AlbumName="Kill 'em All",
                     Url='http://tinysong.com/#/share/hit the lights/14463747'),
                Song(SongID='3', SongName='Motorbreath', ArtistID='1',
                     ArtistName='Metallica', AlbumID='1', AlbumName="Kill 'em All",
                     Url='http://tinysong.com/#/share/hit the lights/14463747'),
                Song(SongID='4', SongName='Jump in the Fire', ArtistID='1',
                     ArtistName='Metallica', AlbumID='1', AlbumName="Kill 'em All",
                     Url='http://tinysong.com/#/share/hit the lights/14463747'),
                Song(SongID='5', SongName='(Anesthesia) Pulling Teath', ArtistID='1',
                     ArtistName='Metallica', AlbumID='1', AlbumName="Kill 'em All",
                     Url='http://tinysong.com/#/share/hit the lights/14463747'),
            ]

        return {'q': q , 'songs': songs}
