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

    def test_increase_entry_fee_in_sales(self):
        self.bar.increase_entry_fee(self.room.price)
        self.assertEqual(12.99, self.bar.total_sales())

    def test_increase_drink_price_in_sales(self):
        self.bar.increase_drink_price(self.drink.price)
        self.assertEqual(8.99, self.bar.total_sales())
    
    def test_increase_food_price_in_sales(self):
        self.bar.increase_food_price(self.food.price)
        self.assertEqual(12.99, self.bar.total_sales())