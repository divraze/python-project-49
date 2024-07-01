import random
from brain_games.game_process import game_process


manual = 'Answer "yes" if the number is even, otherwise answer "no".'

def even_game_logic():

    number = random.randint(1, 100)

    if number % 2 == 0:
        answer = 'yes'
    elif number % 2 != 0:
        answer = 'no'
    return number, answer

def play_even_game():
    game_process(even_game_logic, manual)
