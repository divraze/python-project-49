import random
from brain_games.game_process import game_process


manual = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():

    n = random.randrange(1, 101)

    if n <= 1:
        return n, 'no'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return n, 'no'
    return n, 'yes'


def play_prime_game():
    game_process(is_prime, manual)
