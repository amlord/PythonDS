from stack import Stack

__author__ = 'Lawrence'


def eval_postfix(postfix_exp):
    operand_stack = Stack()
    token_list = postfix_exp.split()
    numeral = "0123456789"
    for token in token_list:
        if token in numeral:
            operand_stack.push(int(token))
        else:
            # token is an operator (+, -, *, / or ^)
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            val = eval_arithmetic(token, operand_1, operand_2)
            operand_stack.push(val)
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
        print("eval_arithmetic: illegal operator.")
        raise SyntaxError