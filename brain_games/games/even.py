import random


MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(a):
    if a % 2 == 0:
        return 'yes'
    return 'no'


def get_even():
    number = random.randint(1, 100)
    answer = is_even(number)
    return number, answer
