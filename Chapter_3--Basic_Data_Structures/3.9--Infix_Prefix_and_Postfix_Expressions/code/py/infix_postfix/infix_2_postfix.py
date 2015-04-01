from stack import Stack

__author__ = 'Lawrence'

def infix_2_postfix(infix_exp):
    """
    Convert an infix expression into its equivalent postfix counterpart.
    :param infix_exp: The infix expression to be converted from. Assume the
                      infix expression is a string of tokens delimited by
                      spaces. The operator tokens are *, /, + and -, along
                      with the left and right parentheses, (and). The operand
                      tokens are the single-character identifiers A, B, C,
                      and so on.
    :return: The equivalent postfix expression compared to the infix one.
    """
    precedences = {}
    precedences["*"] = 3
    precedences["/"] = 3
    precedences["+"] = 2
    precedences["-"] = 2
    precedences["("] = 1
    operator_stack = Stack()
    infix_list = infix_exp.split()
    postfix_list = []
    for token in infix_list:
        if (token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") or (token in "0123456789"):
            postfix_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            # pop the operator_stack until the corresponding left parenthesis
            #  is removed. Append each operator to the end of the output list.
            top_operator = operator_stack.pop()
            while top_operator != '(':
                postfix_list.append(top_operator)
                top_operator = operator_stack.pop()
        else:
            # token is an operator, *, /, +, or -, push it on the
            # operator_stack. However, first remove any operators already on
            # the operator_stack that have higher or equal precedence and
            # append them to the output list.
            while (not operator_stack.is_empty()) and \
                (precedences[operator_stack.peek()] >= precedences[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)
    # When the input expression has been completely processed, check the
    # operator_stack. Any operators still on the stack can be removed and
    # appended to the end of the output list.
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    return " ".join(postfix_list)