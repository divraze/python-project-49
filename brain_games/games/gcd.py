import random


MANUAL = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_num, second_num):
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    if first_num != 0:
        return first_num
    return second_num


def get_question_and_answer():
    first_num, second_num = random.randint(1, 30), random.randint(1, 30)
    question = f'{first_num} {second_num}'
    answer = get_gcd(first_num, second_num)
    return question, answer
