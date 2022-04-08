import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Anna", 100)
    
    def test_guest_has_name(self):
        self.assertEqual("Anna", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)