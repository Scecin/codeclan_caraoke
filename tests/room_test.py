import unittest

from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Anna", 100, "Dancing Queen")
        self.guest_2 = Guest("David", 200, "Wannabe")
        self.guest_3 = Guest("Emma", 150, "Bohemian Rhapsody")
        self.guest_4 = Guest("Tom", 50, "Don't Stop Believin")
        self.guest_5 = Guest("Sean", 10, "Shallow")

        self.bar = Bar(0)

        guests = [self.guest_1, self.guest_2, self.guest_3]

        self.song_1 = Song( "Dancing Queen", "ABBA")
        self.song_2 = Song ("I'm Gonna Be (500 Miles)", "The Proclaimers")
        self.song_3 = Song( "Sweet Caroline", "Neil Diamond")

        songs = [self.song_1, self.song_2]

        self.room = Room("Lucky voice", guests, songs, 12.99, self.bar)
    
    def test_room_has_name(self):
        self.assertCountEqual("Lucky voice", self.room.name)
    
    def test_room_has_price(self):
        self.assertEqual(12.99, self.room.price)
    
    def test_total_guests_in_room(self):
        self.assertEqual(3, self.room.total_guests_in_room())

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song_3)
        self.assertEqual(3, self.room.total_songs_in_room())
    
    def test_remove_song_from_list(self):
        self.room.remove_song_from_room(self.song_2)
        self.assertEqual(1, self.room.total_songs_in_room())

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest_to_room(self.guest_4, self.room)
        self.assertEqual(4, self.room.total_guests_in_room())

    def test_check_out_guests_froom_room(self):
        self.room.check_out_guests_from_room(self.guest_2)
        self.assertEqual(2, self.room.total_guests_in_room())

    def test_check_room_is_full(self):
        self.room.check_in_guest_to_room(self.guest_4, self.room)
        self.assertEqual("Sorry, the room is full. Please try again later.",
        self.room.check_in_guest_to_room(self.guest_4, self.room))
    
    def test_check_not_enought_founds(self):
        self.room.check_in_guest_to_room(self.guest_5, self.room)
        self.assertEqual( "Funds are insufficient. Please try again later.",
        self.room.check_in_guest_to_room(self.guest_5, self.room)) 

    def test_check_room_has_favourite_song(self):
        self.assertEqual("Whoo!", self.room.favourite_song_in_room(self.guest_1.favourite_song))
    
    def test_check_sell_ticket_in_bar_reduce_guest_cash(self):
        self.room.sell_entry_fee(self.guest_1, self.bar, self.room.price)
        self.assertEqual(87.01, self.guest_1.cash)

    def test_check_sell_ticket_in_bar_increase_bar_sales(self):
        self.room.sell_entry_fee(self.guest_1, self.bar, self.room.price)
        self.assertEqual(12.99, self.bar.sales)