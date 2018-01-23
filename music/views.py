from .models import *
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from .forms import PostForm, CommentForm
from django.contrib import messages
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }

    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        if selected_song.is_favorite == False:
            selected_song.is_favorite = True
            selected_song.save()
            return render(request, 'music/detail.html', {'album': album})
        else:
            selected_song.is_favorite = False
            selected_song.save()
            return render(request, 'music/detail.html', {'album': album})
def album_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print form.errors
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            messages.success(request, 'a new album with the title {} has been created.'.format(album.album_title))  # wiadomosc o nowym poscie
            return redirect('http://127.0.0.1:8000/music/{}/'.format(album.pk))

    else:
        form = PostForm()
        return render(request, 'music/album_new.html', {'form': form})

def edit_album(request, album_id):
    album_id = int(album_id)
    album = get_object_or_404(Album, pk=album_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=album)
        if form.is_valid():
            album.artist = form.cleaned_data['artist']
            album.album_title = form.cleaned_data['album_title']
            album.genre = form.cleaned_data['genre']
            album.publication_date = form.cleaned_data['publication_date']
            album.album_logo = form.cleaned_data['album_logo']
            album.edit_date = datetime.datetime.now()
            form.save()
            return redirect('http://127.0.0.1:8000/music/{}/'.format(album.pk))

    else:
        form = PostForm()

    form = PostForm(initial={
                    'artist': album.artist,
                    'album_title': album.album_title,
                    'genre': album.genre,
                    'publication_date': album.publication_date,
                    'album_logo': album.album_logo
                    })
    return render(request, 'music/edit_album.html', {'form': form})

def delete_album_confirmation(request, album_id):
    if request.method == 'POST':
        return delete_album(request, album_id)
    return render(request, 'music/delete_confirmation.html')

def delete_album(request, album_id):
    album_id = int(album_id)
    album = get_object_or_404(Album, pk=album_id)
    print(Album.objects.filter(id=album_id))
    album.delete()
    return redirect('http://127.0.0.1:8000/music/'.format(album.pk))

def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('music:index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/music/')
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def add_comment_to_post(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.album = album
            comment.author = request.user
            comment.save()
            return redirect('http://127.0.0.1:8000/music/'.format(album.pk))
    else:
        form = CommentForm()
    return render(request, 'music/add_comment_to_post.html', {'form': form})