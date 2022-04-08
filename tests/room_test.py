import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Anna", 100)
        self.guest_2 = Guest("David", 200)
        self.guest_3 = Guest("Sean", 50)

        guests = [self.guest_1, self.guest_2]

        self.song_1 = Song( "Dancing Queen", "ABBA")
        self.song_2 = Song ("I'm Gonna Be (500 Miles)", "The Proclaimers")
        self.song_3 = Song( "Sweet Caroline", "Neil Diamond")

        songs = [self.song_1, self.song_2]

        self.room = Room("Lucky voice", guests, songs)
    
    def test_room_has_name(self):
        self.assertCountEqual("Lucky voice", self.room.name)
    
    def test_total_guests_in_room(self):
        self.assertEqual(2, self.room.total_guests_in_room())

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest_to_room(self.guest_3)
        self.assertEqual(3, self.room.total_guests_in_room())

    def test_check_out_guests_froom_room(self):
        self.room.check_out_guests_from_room(self.guest_2)
        self.assertEqual(1, self.room.total_guests_in_room())
    
    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song_3)
        self.assertEqual(3, self.room.total_songs_in_room())
    
    def test_remove_song_from_list(self):
        self.room.remove_song_from_room(self.song_2)
        self.assertEqual(1, self.room.total_songs_in_room())
