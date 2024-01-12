from django.shortcuts import render,get_object_or_404
from .models import Song , Artist
from django.db.models import Count

# Create your views here.

def dashboard(request):
    songs = Song.objects.all()
    artist = Artist.objects.all()
    
    context = {
        'songs':songs,
        'artist':artist
    }
    
    return render(request, 'trial.html',context)

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'song_detail.html', {'song': song})

def trial(request):
    songs = Song.objects.order_by('-id')[:6]
    artist = Artist.objects.all()
    
    context = {
        'songs':songs,
        'artist':artist
    }
    return render(request, 'trial.html',context)

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    context = {'artist': artist}
    return render(request, 'artist_detail.html', context)

def songs(request):
    songs = Song.objects.all()
    
    context = {
        'songs':songs,
    }
    
    return render(request, 'songs.html',context)


def artists(request):
    artists_list = Artist.objects.annotate(song_count=Count('songs'))

    context = {
        'artists_list': artists_list,
    }

    return render(request, 'artists.html', context)

    
