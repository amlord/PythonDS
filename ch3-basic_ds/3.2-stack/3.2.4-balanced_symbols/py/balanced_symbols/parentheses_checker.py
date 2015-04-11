from stack import Stack

__author__ = 'Lawrence'

def is_balanced(symbol_string):
    stack = Stack()
    balanced = True
    index = 0
    while index<len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            top = stack.pop()
            if not match(top, symbol):
                balanced = False
        index = index + 1

    if stack.is_empty() and balanced:
        return True
    else:
        return False

def match(symbol_1, symbol_2):
    opens = "([{"
    closes = ")]}"
    if opens.index(symbol_1) == closes.index(symbol_2):
        return True
    else:
        return False