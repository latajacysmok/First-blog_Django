from django import forms
from .models import Album, Comment, Profile, Song

class PostForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('artist',
                  'album_title',
                  'genre',
                  'publication_date',
                  'album_logo',)
        widgets = {
          'publication_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'avatar', 'gender', 'age', 'aboutMe', 'city', 'country', 'email']
        widgets = {'description': forms.Textarea(attrs={'cols': 30, 'rows': 10})
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['album',
                  'song_title',]