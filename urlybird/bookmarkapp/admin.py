from django.contrib import admin
from bookmarkapp.models import Bookmark

# Register your models here.


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'original_url', 'short_url', 'timestamp', 'author']

admin.site.register(Bookmark, BookmarkAdmin)
