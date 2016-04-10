from django.db import models


class Album(models.Model):
    """Album model for music app"""
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_art = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' by ' + self.artist


class Song(models.Model):
    """Song model for albums in music app"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + '.' + self.file_type
