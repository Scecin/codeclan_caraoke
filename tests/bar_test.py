import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song
from src.bar import Bar
from src.drink import Drink
from src.food import Food

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(0)

        self.drink = Drink("cocktail", 8.99)

        self.food = Food("nachos", 12.99)

        self.guest = Guest("Anna", 100, "Dancing Queen")
        self.guest_2 = Guest("Sean", 10, "Wannabe")

        self.song = Song( "Dancing Queen", "ABBA")

        self.room = Room("Lucky voice", self.guest, self.song, 12.99, 0)

    def test_bar_has_sales(self):
        self.assertEqual(0, self.bar.sales)

    def test_sell_ticket(self):
        self.assertEqual(12.99, self.bar.sell_ticket(self.room.price))
    
    def test_sell_food(self):
        self.assertEqual(12.99, self.bar.sell_food(self.food.price))

    def test_sell_drink(self):
        self.assertEqual(8.99, self.bar.sell_drink(self.drink.price))

    def test_total_sales(self):
        self.assertEqual(0, self.bar.total_sales())