from unittest import TestCase
from eval_postfix import eval_postfix

__author__ = 'Lawrence'


class TestEval_postfix(TestCase):
    def test_eval_postfix(self):
        self.assertEqual(
            eval_postfix(""),
            None,
            "The value of postfix expression '' is not None.")
        self.assertEqual(
            eval_postfix("9 9 + 3 2 ^ /"),
            2.0,
            "The value of postfix expression '9 9 + 3 2 ^ /' is not 2.0.")
        with self.assertRaises(SyntaxError):
            eval_postfix("9 9 + 3 2 ^ /##@@")