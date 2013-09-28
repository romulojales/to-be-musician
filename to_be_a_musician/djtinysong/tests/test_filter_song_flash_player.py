import unittest

from django.template.base import Template
from django.template.context import Context

from djtinysong.templatetags.tinysong import flash_player


class TestModels(unittest.TestCase):
    def test_render_html_flash(self):
        template = Template('{% load tinysong %}{{songID|flash_player}}')
        context = Context({"songID": 123})
        rendered = template.render(context)
        from_function = flash_player(123)
        self.assertEquals(rendered, from_function)
