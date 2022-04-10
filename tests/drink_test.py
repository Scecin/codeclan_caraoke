import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
       self.drink = Drink("cocktail", 8.99)

    def test_drink_has_name(self):
        self.assertEqual("cocktail", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(8.99, self.drink.price)