import random


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):

    if a <= 1:
        return 'no'
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return 'no'
    return 'yes'


def get_prime():

    num = random.randrange(1, 101)
    answer = is_prime(num)
    return num, answer
