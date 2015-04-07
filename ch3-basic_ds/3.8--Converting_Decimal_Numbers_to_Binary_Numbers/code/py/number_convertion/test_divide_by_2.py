from unittest import TestCase
from number_convertion import divide_by_2

__author__ = 'Lawrence'


class TestDivide_by_2(TestCase):
    def test_divide_by_2(self):
        self.assertEqual(
            divide_by_2(0),
            "0",
            "The binary representation of decimal number 0 is not 0.")
        self.assertEqual(
            divide_by_2(42),
            "101010",
            "The binary representation of decimal number 42 is not 101010.")