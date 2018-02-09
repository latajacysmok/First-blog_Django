from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

import datetime

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    publication_date = models.DateField(null=True, blank=True)
    album_logo = models.ImageField(upload_to="music/static/music/images/", default=settings.DEFAULT_URL)
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
    author = models.ForeignKey(User)
    comment = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    edit_date = models.DateField(null=True)

    def __str__(self):
        return self.comment

class Profile(models.Model):
    Gender = (
		('MEN', 'Mężczyzna'),
		('Women', 'Kobieta'),
		('Other', 'Inna')
	)
    Age = (
        [(i, i) for i in range(100)]
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True)
    avatar = models.ImageField(upload_to='music/static/music/images/avatars/', default='music/static/music/images/avatars/default.png')
    gender = models.CharField(max_length=12, choices=Gender, null=True)
    age = models.IntegerField(null=True, choices=Age)
    aboutMe = models.TextField(null=True)
    city = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=70,blank=True)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)