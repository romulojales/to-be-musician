from django import template
from django.utils.safestring import SafeString

register = template.Library()


@register.filter
def flash_player(song_id):
    return SafeString('''<embed src="http://grooveshark.com/songWidget.swf"
        type="application/x-shockwave-flash"
        width="250"
        height="40"
        flashvars="hostname=cowbell.grooveshark.com&amp;songIDs=%s&amp;style=metal&amp;p=0"
        allowscriptaccess="always"
        wmode="window">''' % song_id)
