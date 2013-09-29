from django.contrib import admin
from songs.models import Artist, Album, Song, Interpretation


class SongsBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_id')


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'album', )


admin.site.register(Artist, SongsBaseAdmin)
admin.site.register(Album, SongsBaseAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Interpretation)
