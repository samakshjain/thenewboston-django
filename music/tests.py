from django.test import TestCase, Client
from music.models import Album, Song


class modelCreateTests(TestCase):
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

    def test_album_created(self):
        EpicAlbum = Album.objects.get(album_title="EpicTitle")
        self.assertEqual(str(EpicAlbum), "EpicTitle by GuitarGod")

    def test_song_creted(self):
        RockAnthem = Song.objects.get(song_title="RockAnthem")
        self.assertEqual(str(RockAnthem), "RockAnthem.mp3")


class urlTests(TestCase):
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
        self.c = Client()

    def test_requests(self):
        music_response = self.c.get('/music/')
        album_response = self.c.get('/music/1/')
        favourite_response = self.c.post('/music/1/favourite/', {'song': 1})
        self.assertEqual(music_response.status_code, 200)
        self.assertEqual(album_response.status_code, 200)
        self.assertEqual(favourite_response.status_code, 200)

    def test_exceptions(self):
        favourite_response = self.c.post('/music/1/favourite')
        self.assertEqual(favourite_response.status_code, 301)
