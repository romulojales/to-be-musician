from django import forms
from django.utils.translation import ugettext_lazy as _
from songs.models import Interpretation


class InterpretationForm(forms.ModelForm):

    class Meta:
        model = Interpretation
        exclude = ('user', 'song', 'created_at', 'last_update', )

    def clean(self):
        cleaned_data = super(InterpretationForm, self).clean()

        some_field_filled = (self.cleaned_data.get('description') or
                             self.cleaned_data.get('youtube_url') or
                             self.cleaned_data.get('songsterr_url') or
                             self.cleaned_data.get('soundcloud_url'))

        if not some_field_filled:
            raise forms.ValidationError(_('You must filled at least one field bellow'))

        return cleaned_data

    def save(self, user, song, *args, **kwargs):
        self.instance.user = user
        self.instance.song = song

        return super(InterpretationForm, self).save(*args, **kwargs)
