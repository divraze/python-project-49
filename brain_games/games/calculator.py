import random


MANUAL = 'What is the result of the expression?'


def get_calculator():
    first_num, second_num = random.randint(1, 10), random.randint(1, 10)
    signs = random.choice(['+', '-', '*'])
    expression = f'{first_num} {signs} {second_num}'
    result = eval(expression)
    return expression, result


def get_question_and_answer():
    question, answer = get_calculator()
    return question, answer
