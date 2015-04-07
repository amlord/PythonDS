from stack import Stack

__author__ = 'Lawrence'


def divide_by_2(decimal_number):
    remainder_stack = Stack()
    while decimal_number > 0:
        remainder = decimal_number % 2
        remainder_stack.push(remainder)
        decimal_number = decimal_number // 2
    binary_string = ""
    while not remainder_stack.is_empty():
        binary_string = binary_string + str(remainder_stack.pop())
    if binary_string == "":
        binary_string = "0"
    return binary_string

def base_converter(decimal_number, base):
    digits = "0123456789ABCDEF"
    remainder_stack = Stack()
    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.push(remainder)
        decimal_number = decimal_number // base
    binary_string = ""
    while not remainder_stack.is_empty():
        binary_string = binary_string + str(digits[remainder_stack.pop()])
    if binary_string == "":
        binary_string = "0"
    return binary_string