# spotlight/urls.py
from django.urls import path
from .views import artist_detail, dashboard,song_detail,songs,artists,add_artist,add_song

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('songs/', songs, name='songs'),
    path('artists/', artists, name='artists'),
    # path('trial/', trial, name='trial'),
    path('add_artist/', add_artist, name='add_artist'),
    path('add_song/', add_song, name='add_song'),
    path('songs/<int:song_id>/', song_detail, name='song_detail'),
    path('artist/<int:artist_id>/', artist_detail, name='artist_detail'),
]
