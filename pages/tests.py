import os

from django.test import TestCase
from django.test import Client

from .utils import get_posts_data
from .templatetags.pages_tags import page_url


class BasicTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def testHome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'http://djangogirls.org/taipei')

    def testTutorialList(self):
        posts_data = get_posts_data(os.path.join('pages', 'posts', 'info.json'))

        response = self.client.get('/tutorials/')
        for track in posts_data['tutorials']['tracks']:
            for post in track['posts']:
                if post['target'].startswith('//') or '://' in post['target']:
                    continue
                post_block = (
                    '<a href="/{target}/">'
                    '<div class="tutorial-item">'
                    '<h3>{title}</h3>'
                    '<p>{description}</p>'
                    '</div>'
                    '</a>'
                ).format(
                    target=post['target'], title=post['title'],
                    description=post['description'],
                )
                self.assertContains(response, post_block, html=True)

    def testTutorialDetail(self):
        data = get_posts_data(os.path.join('pages', 'posts', 'info.json'))

        for track in data['tutorials']['tracks']:
            for post in track['posts']:
                if post['target'].startswith('//') or '://' in post['target']:
                    continue
                response = self.client.get(page_url(post['target']))
                self.assertContains(response, post['title'])
