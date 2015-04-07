from eval_infix import eval_infix

__author__ = 'Lawrence'

def infix_evaluator():
    welcome = "Please input an infix expression to evaluate, tokens should\n "\
        "be single digits (0-9) and delimited by space. The accessible\n " \
        "arithmetic operators includes ^, *, /, + and -. Parentheses can\n " \
        "be use to force precedences. Input 'quit' to exit the program.\n " \
        "e.g.\n"\
        "Infix expression to evaluate: '( 2 + ( 3 - 1 ) ) ^ 2'\n"\
        "16\n"\
        "Infix expression to evaluate: '( 7 + 8 ) / ( 3 + 2 )'\n"\
        "3\n"\
        "Infix expression to evaluate: 'quit'\n"\
        "<command-line> $ \n"
    prompt = "Infix expression to evaluate: "
    print(welcome)
    user_input = input(prompt)
    while user_input != 'quit':
        val = eval_infix(user_input)
        print(val)
        user_input = input(prompt)

# Run the evaluator
if __name__ == '__main__':
    infix_evaluator()