import random
from brain_games.game_process import game_process


manual = 'Find the greatest common divisor of given numbers.'


def gcd_game_logic():

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    question = f'{num_1} {num_2}'

    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    if num_1 != 0:
        return question, num_1
    return question, num_2


def play_gcd_game():
    game_process(gcd_game_logic, manual)
