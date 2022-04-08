from turtle import clear
import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song= Song( "Dancing Queen", "ABBA")

    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song.name)

    def test_song_has_singer(self):
        self.assertEqual("ABBA", self.song.singer)