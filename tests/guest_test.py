import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Anna", 100)
        self.guest_2 = Guest("Sean", 10)

        self.song = Song( "Dancing Queen", "ABBA")

        self.room = Room("Lucky voice", self.guest, self.song, 12.99)
    
    def test_guest_has_name(self):
        self.assertEqual("Anna", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)
    
    def test_has_sufficient_founds(self):
        self.assertEqual(True, self.guest.sufficient_founds(self.room))

    def test_not_have_sufficient_founds(self):
        self.assertEqual(False, self.guest_2.sufficient_founds(self.room))

    def test_pay_entry_fee(self):
        self.assertEqual(87.01, self.guest.pay_entry_fee(self.room))
    
    # def test_pay_entry_fee(self, guest,room):