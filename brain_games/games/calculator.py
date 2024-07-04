import random


MANUAL = 'What is the result of the expression?'


def get_calc():

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    signs = random.choice(['+', '-', '*'])
    expression = f'{num_1} {signs} {num_2}'
    answer = eval(expression)
    return expression, answer
