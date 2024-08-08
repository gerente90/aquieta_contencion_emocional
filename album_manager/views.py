from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Artist, Album
from .forms import ArtistForm, AlbumForm

def index(request):
    albums = Album.objects.order_by('title')  # Obtener todos los álbumes
    return render(request, 'index.html', {'albums': albums})



def artist (request):
    artists = Artist.objects.order_by('name')
    template = loader.get_template('artist.html')
    return HttpResponse(template.render({'artists': artists}, request))

def album (request):
    albums = Album.objects.order_by('title')
    template = loader.get_template('album.html')
    return HttpResponse(template.render({'albums': albums}, request))

def display_artist (request, artist_name):
    artist = Artist.objects.get(name=artist_name)
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def display_album (request, album_title):
    album = Album.objects.get(title=album_title)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def add_artist (request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artist')
    else:
        form = ArtistForm()

    return render(request, 'artist_form.html', {'form':form})

def add_album (request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:album')
    else:
        form = AlbumForm()

    return render(request, 'album_form.html', {'form':form})

def edit_artist (request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artist')
    else:
        form = ArtistForm(instance=artist)

    return render(request, 'artist_form.html', {'form':form})

def edit_album (request, album_title):
    album = get_object_or_404(Album, title=album_title)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:album')
    else:
        form = AlbumForm(instance=album)

    return render(request, 'album_form.html', {'form':form})

def delete_artist (request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    artist.delete()
    return redirect("album_manager:artist")

def delete_album (request, album_title):
    album = get_object_or_404(Album, title=album_title)
    album.delete()
    return redirect("album_manager:album")