from unittest import TestCase
from infix_2_postfix import infix_2_postfix

__author__ = 'Lawrence'


class TestInfix_2_postfix(TestCase):
    def test_infix_2_postfix(self):
        self.assertEqual(
            infix_2_postfix(""),
            "",
            "The postfix counterpart of infix expression `' is not `'.")
        self.assertEqual(
            infix_2_postfix("( A + B ) * ( C + D )"),
            "A B + C D + *",
            "The postfix counterpart of infix expression " +
            "`( A + B ) * ( C + D )' is not `A B + C D + *'.")
        self.assertEqual(
            infix_2_postfix("( A + B ) * C"),
            "A B + C *",
            "The postfix counterpart of infix expression " +
            "`( A + B ) * C' is not `A B + C *'.")
        self.assertEqual(
            infix_2_postfix("A + B * C"),
            "A B C * +",
            "The postfix counterpart of infix expression " +
            "`A + B * C' is not `A B C * +'.")