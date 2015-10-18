from bs4 import BeautifulSoup
from django.contrib.auth.models import User

from ...models import Bookmark

import requests
import re

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_admin()
        load_bookmarks()


def create_admin():
    User.objects.create_superuser(username='admin',
                                  password='password',
                                  email='')

def load_bookmarks():
    urls_page = BeautifulSoup(requests.get('http://www.mlssoccer.com/')
                              .content, 'html.parser') \
                              .find_all('a', {'banner-club-tablet'})

    links = [re.findall(r'href="(\S+)"', str(anchor)) for anchor in urls_page]
    titles = [re.findall(r'title="(.+)"', str(anchor))for anchor in urls_page]

    # links = re.findall(r'href="(\S+)"', anchor)
    # titles = re.findall(r'title="(.+)"', anchor)


    for a in zip(links, titles):
        bookmark = Bookmark(
            title=a[1][0],
            original_url=a[0][0],
            author=User.objects.get(username='admin'),
            short_url=a[0][0][11:19]  # TODO A better fake short_url generator
        )
        bookmark.save()
