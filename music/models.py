from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

import datetime

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    publication_date = models.IntegerField(null=True)
    album_logo = models.FileField()
    edit_date = models.DateField(null=True)

    def get_absolte_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist + " - " + self.album_title + " " + str(self.publication_date)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

class Comment(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.comment