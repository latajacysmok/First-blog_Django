from .models import *
from django.shortcuts import HttpResponseRedirect, HttpResponse, get_object_or_404, redirect, render
from .forms import PostForm, CommentForm, ProfileForm, SongForm
from django.contrib import messages
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db.models.signals import post_save


def index(request):
    all_albums = Album.objects.all().order_by("-creation_date")
    context = {
        'all_albums': all_albums,
    }

    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    print("album_songs")
    print(Song.objects.filter(album=album))
    context = {
        'album': album,
        'album_songs': Song.objects.filter(album=album),
        'DEFAULT_URL': settings.MEDIA_URL + settings.DEFAULT_URL
    }
    return render(request, 'music/detail.html', context)

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

        else:
            selected_song.is_favorite = False
            selected_song.save()

        return render(request, 'music/detail.html', {'album': album})

def album_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.author = request.user
            album.save()
            messages.success(request, 'a new album with the title {} has been created.'.format(album.album_title))  # wiadomosc o nowym poscie
            return redirect('music:index')
        else:
            return HttpResponse(form.errors)
    else:
        form = PostForm()
        return render(request, 'music/album_new.html', {'form': form})

def song_new(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        print(form.errors)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            messages.success(request, 'a new song with the title {} has been created.'.format(song.song_title))  # wiadomosc o nowym poscie
            return redirect('music:detail', album_id=song.album.id)
        else:
            return HttpResponse(form.errors)
    else:
        form = SongForm()
        return render(request, 'music/song_new.html', {'form': form})

def delete_song(request, album_id):
    album_id = int(album_id)
    album = get_object_or_404(Album, pk=album_id)
    songs = Song.objects.all()
    all_albums = Album.objects.all()
    context = {
        'songs': songs,
        'all_albums': all_albums,
        'album': album,
    }
    return render(request, 'music/song_delete.html', context)

def edit_album(request, album_id):
    album_id = int(album_id)
    album = get_object_or_404(Album, pk=album_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album.artist = form.cleaned_data['artist']
            album.album_title = form.cleaned_data['album_title']
            album.genre = form.cleaned_data['genre']
            album.publication_date = form.cleaned_data['publication_date']
            album.album_logo = form.cleaned_data['album_logo']
            album.edit_date = datetime.datetime.now()
            form.save()
            return redirect('music:detail', album_id=album_id)

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
    return redirect('music:index')

def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('music:detail', album_id=comment.album.id)

def edit_comment(request, comment_id):
    comment_id = int(comment_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.author = request.user
            comment.comment = form.cleaned_data['comment']
            # comment.created_date = form.cleaned_data['created_date']
            comment.edit_date = datetime.datetime.now()
            form.save()
            return redirect('music:detail', album_id=comment.album.id)
    else:
        form = CommentForm()

    form = CommentForm(initial={
        'author': comment.author,
        'comment': comment.comment,
        'created_date': comment.created_date,
    })
    return render(request, 'music/edit_comment.html', {'form': form})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.description = form.cleaned_data['description']
            profile.avatar = form.cleaned_data['avatar']
            form.save()
            return HttpResponseRedirect('/music/')

    form = ProfileForm(initial={
        'description': profile.description,
        'avatar': profile.avatar,
        'gender': profile.gender,
        'age': profile.age,
        'aboutMe': profile.aboutMe,
        'city': profile.city,
        'country': profile.country,
        'email': profile.email
        })
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'music/editprofile.html', context)

def view_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {
        'profile': profile
    }
    return render(request, 'music/profile.html', context)


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
            return redirect('music:detail', album_id=album_id)
    else:
        form = CommentForm()
    return render(request, 'music/add_comment_to_post.html', {'form': form})


def songs(request):
    songs = Song.objects.all()
    all_albums = Album.objects.all()
    context = {
        'songs': songs,
        'all_albums': all_albums,
    }
    return render(request, 'music/songs.html', context)

def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        profile = Profile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User) # WAZNE

