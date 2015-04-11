from unittest import TestCase
from parentheses_checker import is_balanced

__author__ = 'Lawrence'


class TestIs_balanced(TestCase):
    def test_is_paren_balanced(self):
        self.assertTrue(
            is_balanced(""),
            "The parentheses string `' are not balanced.")
        self.assertTrue(
            is_balanced("((()))"),
            "The parentheses string `((()))' are not balanced.")
        self.assertFalse(
            is_balanced("(()"),
            "The parentheses string `(()' are balanced.")