from stack import Stack

__author__ = 'Lawrence'

def infix_2_postfix(infix_exp):
    """
    Convert an infix expression into its equivalent postfix counterpart.
    :param infix_exp: The infix expression to be converted from. Assume the
                      infix expression is a string of tokens delimited by
                      spaces. The operator tokens are *, /, + and -, along with
                      the left and right parentheses, (and). The operand tokens
                      are the single-character identifiers A, B, C, and so on.
    :return: The equivalent postfix expression compared to the infix one.
    """
    precedence = {}
    precedence['^'] = 4
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1
    operator_stack = Stack()
    infix_list = infix_exp.split()
    postfix_list = []
    alphnums = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    operators = "^*/+-"

    for token in infix_list:
        if token in alphnums:
            postfix_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            # pop the operator_stack until the corresponding left parenthesis
            #  is removed. Append each operator to the end of the output list.
            top_token = operator_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operator_stack.pop()
        elif token in operators:
            # token is ^, *, /, +, or -, push it on the operator_stack. However,
            # first remove any operators already on the operator_stack that have
            # higher or equal precedence and append them to the output list.
            while ((not operator_stack.is_empty()) and
                (precedence[operator_stack.peek()] >= precedence[token])):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)
        else:
            # illegal token raise exception
            raise(SyntaxError)
    # When the input expression has been completely processed, check the
    # operator_stack. Any operators still on the stack can be removed and
    # appended to the end of the output list.
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    return ' '.join(postfix_list)