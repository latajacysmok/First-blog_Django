from django.contrib import admin
from .models import Album, Song, Comment, Profile

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Profile)
