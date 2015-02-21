import os

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from .utils import get_posts_data
from .templatetags.pages_tags import page_url


class BasicTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def testHome(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'http://djangogirls.org/taipei')

    def testTutorials(self):
        data = get_posts_data(os.path.join('pages', 'posts', 'info.json'))

        for track in data['tutorials']['tracks']:
            for post in track['posts']:
                if post['target'].startswith('//') or '://' in post['target']:
                    continue
                response = self.client.get(page_url(post['target']))
                self.assertContains(response, post['title'])
