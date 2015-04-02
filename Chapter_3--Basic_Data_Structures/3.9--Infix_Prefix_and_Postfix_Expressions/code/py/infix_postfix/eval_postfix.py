from stack import Stack

__author__ = 'Lawrence'


def eval_postfix(postfix_exp):
    """
    Evaluate the value of an postfix expression.
    :param postfix_exp: The postfix expression to be evaluated. Assume the
                        postfix expression is a string of tokens delimited by
                        spaces. The operator tokens are ^, *, /, + and -. The
                        operand tokens are the single-character identifiers A,
                        B, C, and so on.
    :return: value of the postfix expression
    """
    operand_stack = Stack()
    token_list = postfix_exp.split()
    numeral = "0123456789"
    operators = "^*/+-"
    for token in token_list:
        if token in numeral:
            operand_stack.push(int(token))
        elif token in operators:
            # token is an operator (+, -, *, / or ^)
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            val = eval_arithmetic(token, operand_1, operand_2)
            operand_stack.push(val)
        else:
            print("eval_postfix: illegal operator, " + token)
            raise(SyntaxError)
    if operand_stack.is_empty():
        return None
    else:
        return operand_stack.pop()

def eval_arithmetic(operator, operand_1, operand_2):
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2
    elif operator == '^':
        return operand_1 ** operand_2
    else:
        print("eval_arithmetic: illegal operator, " + operator)
        raise(SyntaxError)