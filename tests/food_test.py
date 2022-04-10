import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("nachos", 12.99)

    def test_food_has_name(self):
        self.assertEqual("nachos", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(12.99, self.food.price)