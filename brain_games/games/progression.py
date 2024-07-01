import random
from brain_games.game_process import game_process


manual = 'What number is missing in the progression?'


def progression_game_logic():

    first_num = random.randrange(1, 100)
    step = random.randrange(1, 6)
    progression = [first_num + step * i for i in range(10)]
    index = random.randrange(1, 10)
    hidden_index = progression[index]
    progression[index] = '..'
    str_progression = [str(i) for i in progression]
    progression_finish = ' '.join(str_progression)

    return progression_finish, hidden_index


def play_progression_game():
    game_process(progression_game_logic, manual)
