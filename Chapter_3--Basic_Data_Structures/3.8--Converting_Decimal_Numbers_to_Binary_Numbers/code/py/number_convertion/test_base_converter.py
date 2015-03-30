from unittest import TestCase
from number_convertion import base_converter

__author__ = 'Lawrence'


class TestBase_converter(TestCase):
    def test_base_converter(self):
        self.assertEqual(
            base_converter(0,2),
            "0",
            "The binary representation of decimal number 0 is not 0.")
        self.assertEqual(
            base_converter(25,2),
            "11001",
            "The binary representation of decimal number 25 is not 11001.")
        self.assertEqual(
            base_converter(0,8),
            "0",
            "The octal representation of decimal number 0 is not 0.")
        self.assertEqual(
            base_converter(25,8),
            "31",
            "The octal representation of decimal number 25 is not 31.")
        self.assertEqual(
            base_converter(0,16),
            "0",
            "The hexadecimal representation of decimal number 0 is not 0.")
        self.assertEqual(
            base_converter(256,16),
            "100",
            "The hexadecimal representation of decimal number 256 is not 100.")