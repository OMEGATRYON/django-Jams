from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # image = models.Image////
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.DateField()
    # cover_art = models.Image////

class Song(models.Model):
    name = models.CharField(max_length=500)
    duration = models.IntegerField()
    artist = models.ManyToManyField(Artist, through='ArtistSong')
    
class Genre(models.Model):
    name = models.CharField(max_length=500)

class Playlist(models.Model):
    name = models.CharField(max_length=500)
    songs = models.ManyToManyField(Song, through='PlaylistSong')

class PlaylistSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

class ArtistSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('artist', 'song')