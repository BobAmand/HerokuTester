from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Two models will be built.
    - Bookmark will:
        > capture the title + description of site bookmarked.
        > note the original URL and translate to a short URL.
        > note the time of bookmark selection (click).
         >> distinguish between initial and return?
         >> distinquish between adding and deleting?
         >> distinquish between logon + logoff (time on site)?
        > link the data to a User.
    - Click will:
        > time stamp each time the bookmark is used by user.
        > many clicks for one user.
        > many clicks for many users.
'''


class Bookmark(models.Model):

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True)
    original_url = models.URLField()  # max_length is 200 default.
    short_url = models.CharField(max_length=7)  # assuming 7 characters
    timestamp = models.DateTimeField(auto_now_add=True)  # save every click
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User)

class Click(models.Model):

    # ADD = 'A'
    # DEL = 'D'
    # USE = 'U'
    # ACTIVITY_SELECT = (
    #     (ADD, 'A'),
    #     (DEL, 'D'),
    #     (USE, 'U'),
    # )
    #
    # activty = models.CharField(max_length=1, choices=ACTIVITY_SELECT)

    timestamp = models.DateTimeField(auto_now_add=True)  # save every click
    bookmark = models.ForeignKey(Bookmark)
