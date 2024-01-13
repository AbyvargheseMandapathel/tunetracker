from django.shortcuts import redirect, render,get_object_or_404
from .models import Song , Artist
from django.db.models import Count
from .forms import ArtistForm,SongForm

# Create your views here.

def dashboard(request):
    songs = Song.objects.all().order_by('-id')
    artist = Artist.objects.all()
    
    context = {
        'songs':songs,
        'artist':artist
    }
    
    return render(request, 'index.html',context)


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    songs = Song.objects.filter(artist=artist)
    context = {
        'artist': artist,
        'songs': songs
        }
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

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists')  
    else:
        form = ArtistForm()

    return render(request, 'add_artist.html', {'form': form})


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists')  
    else:
        form = SongForm()

    return render(request, 'add_song.html', {'form': form})


def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'song_detail.html', {'song': song})



    
