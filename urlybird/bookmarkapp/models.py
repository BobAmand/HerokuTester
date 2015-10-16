from django.db import models

# Create your models here.
'''
Two models will be built.
    - Bookmark will:
        > capture the title + description of site bookmarked.
        > note the original URL and translate to a short URL.
        > note the time of selection (click) as a bookmark.
        > link the data to a User.
    - Click will:
        > time stamp each time the bookmark is used by user.
'''


class Bookmark()
