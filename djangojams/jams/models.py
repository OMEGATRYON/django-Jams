from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=500)
    duration = models.IntegerField()
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.DateField()
    # cover_art = models.Image////

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # image = models.Image////

class Genre(models.Model):
    name = models.CharField(max_length=500)

class Playlist(models.Model):
    name = models.CharField(max_length=500)