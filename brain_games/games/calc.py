import random
from brain_games.game_process import game_process


manual = 'What is the result of the expression?'

def calc_game_logic():

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    signs = random.choice(['+', '-', '*'])
    expression = f'{num_1} {signs} {num_2}'
    answer = eval(expression)
    return expression, answer

def play_calc_game():
    game_process(calc_game_logic, manual)
