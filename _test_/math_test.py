import unittest
from faker import Faker
from math_numbers import OddNumber


class TestMathCase(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_odd_number_is_not_none(self):
        number = self.fake.random_number()
        self.assertIsNotNone(OddNumber.odd_number(number))

    def test_return_true_when_odd_number_is_odd(self):
        number = self.fake.random_number() * 2
        self.assertEqual(OddNumber.odd_number(number), True)

    def test_return_false_when_odd_number_is_even(self):
        number = self.fake.random_number() * 2 + 1
        self.assertEqual(OddNumber.odd_number(number), False)
