from django.shortcuts import render,get_object_or_404
from .models import Song , Artist
# Create your views here.

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'song_detail.html', {'song': song})

def trial(request):
    return render(request, 'trial.html')
