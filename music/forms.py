from django import forms

from .models import Album, Comment

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