from unittest import TestCase
from eval_infix import eval_infix

__author__ = 'Lawrence'


class TestEval_infix(TestCase):
    def test_eval_infix(self):
        self.assertEqual(
            eval_infix(""),
            None,
            "The value of infix expression '' is not None.")
        self.assertEqual(
            eval_infix("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8"),
            36,
            "The value of infix expression '1 + 2 + 3 + 4 + 5 + 6 + 7 + 8' " +
            "is not None.")
        self.assertEqual(
            eval_infix("( 9 + 9 ) / ( 3 ^ 2 )"),
            2,
            "The value of infix expression '( 9 + 9 ) / ( 3 ^ 2 )' is not 2.")
        with self.assertRaises(SyntaxError):
            eval_infix("( 9 + 9 ) / ( 3 ^ 2 ) #")