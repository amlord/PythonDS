from unittest import TestCase
from reverse_string import reverse_string

__author__ = 'Lawrence'


class TestReverse_string(TestCase):
    def test_reverse_string(self):
        self.assertEqual(
            reverse_string(""),
            "",
            "The reversion of `'(empty string) is not `'(empty string).")
        self.assertEqual(
            reverse_string("a"),
            "a",
            "The reversion of string 'a' is not string 'a'.")
        self.assertEqual(
            reverse_string("apple"),
            "elppa",
            "The reversion of string 'apple' is not string 'elppa'.")
        self.assertEqual(
            reverse_string("1234567890"),
            "0987654321",
            "The reversion of string '1234567890' is not string '0987654321'.")