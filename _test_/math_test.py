import unittest
from faker import Faker
from math_numbers import OddNumber


class TestMathCase(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_odd_number_is_not_none(self):
        number = self.fake.random_number()
        self.assertIsNotNone(OddNumber.odd_number(number))
