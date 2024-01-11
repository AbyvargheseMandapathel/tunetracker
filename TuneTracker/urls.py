# spotlight/urls.py
from django.urls import path
from .views import song_list,song_detail,trial

urlpatterns = [
    path('', song_list, name='song_list'),
    path('trial/', trial, name='trial'),
    path('songs/<int:song_id>/', song_detail, name='song_detail'),
]
