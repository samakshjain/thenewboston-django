from django.test import TestCase
from models import Album, Song
# Create your tests here.


class AlbumTestCase(TestCase):
    def setUp(self):
        Album.objects.create(
            artist="GuitarGod",
            album_title="EpicTitle",
            genre="ROCK",
            album_art="somealbumart.png")

    def test_album_created(self):
        EpicAlbum = Album.objects.get(album_title="EpicTitle")
        self.assertEqual(str(EpicAlbum), "EpicTitle by GuitarGod")


class SongTestCase(TestCase):
    def setUp(self):
        Album.objects.create(
            artist="GuitarGod",
            album_title="EpicTitle",
            genre="ROCK",
            album_art="somealbumart.png")

        Song.objects.create(
            song_title="RockAnthem",
            file_type="mp3",
            album=Album.objects.get(album_title="EpicTitle"))

    def test_song_creted(self):
        RockAnthem = Song.objects.get(song_title="RockAnthem")
        self.assertEqual(str(RockAnthem), "RockAnthem.mp3")
