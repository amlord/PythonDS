from infix_2_postfix import infix_2_postfix
from eval_postfix import eval_postfix

__author__ = 'Lawrence'

def eval_infix(infix_exp):
    """
    Evaluate the value of an infix expression.
    :param infix_exp: The infix expression to be evaluated. Assume the infix
                      expression is a string of tokens delimited by spaces. The
                      operator tokens are ^, *, /, + and -, along with the left
                      and right parentheses, (and). The operand tokens are the
                      single-character identifiers A, B, C, and so on.
    :return: value of the infix expression
    """
    postfix_exp = infix_2_postfix(infix_exp)
    val = eval_postfix(postfix_exp)
    return val