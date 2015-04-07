from stack import Stack

__author__ = 'Lawrence'

def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    for character in string:
        stack.push(character)
    while not stack.is_empty():
        reversed_string = reversed_string + stack.pop()
    return reversed_string
