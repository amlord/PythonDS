from stack import Stack

__author__ = 'Lawrence'

def is_balanced(paren_string):
    stack = Stack()
    index = 0
    balanced = True
    while index<len(paren_string) and balanced:
        symbol = paren_string[index]
        if symbol == '(':
            stack.push(symbol)
        else:
            if not stack.is_empty():
                stack.pop()
            else:
                balanced = False
        index = index + 1
    if stack.is_empty() and balanced:
        return True
    else:
        return False