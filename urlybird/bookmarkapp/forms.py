from django import forms
from .models import Bookmark
# from bookmarkapp import models


class BookmarkForm(forms.Form):
    '''bkf = bookmark form'''
    title = forms.CharField(max_length=20, required=True)
    description = forms.CharField(max_length=255,
                                  widget=forms.Textarea
                                  )     # removed null=True
    original_url = forms.URLField()  # max_length is 200 default.

    short_url = forms.CharField(max_length=7)  # assuming 7 characters
    timestamp = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')
                                    # removed 'auto_now_add=True'
    # author = forms.ForeignKey(User)



    class Meta:
        model = Bookmark
        fields = ('title', 'description', 'original_url', 'short_url',
                  'timestamp', 'author')



    # short_url = models.CharField(max_length=7)  # assuming 7 characters
    # timestamp = models.DateTimeField(auto_now_add=True)  # save every click
    # author = models.ForeignKey(User)
