import random


MANUAL = 'Find the greatest common divisor of given numbers.'


def has_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a != 0:
        return a
    return b


def get_gcd():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    question = f'{num_1} {num_2}'
    answer = has_gcd(num_1, num_2)
    return question, answer
