from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    spotify_url = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='artist_profiles/', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='artist_covers/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE , related_name='songs')
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='song_covers/', blank=True, null=True)
    music_video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"