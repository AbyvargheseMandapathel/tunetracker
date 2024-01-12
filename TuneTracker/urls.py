# spotlight/urls.py
from django.urls import path
from .views import artist_detail, dashboard,song_detail,trial,songs,artists

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('songs/', songs, name='songs'),
    path('artists/', artists, name='artists'),
    path('trial/', trial, name='trial'),
    path('songs/<int:song_id>/', song_detail, name='song_detail'),
    path('artist/<int:artist_id>/', artist_detail, name='artist_detail'),
]
