import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
       self.drink = Drink("cocktail", 8.99)