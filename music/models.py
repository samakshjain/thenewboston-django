from django.db import models

class Album(models.Model):
    """Album model for music app"""
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_art = models.CharField(max_length=1000)


    def __init__(self, arg):
        super(Album, self).__init__()
        self.arg = arg

class Songs(models.Model):
    """Song model for albums in music app"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __init__(self, arg):
        super(Songs, self).__init__()
        self.arg = arg
        