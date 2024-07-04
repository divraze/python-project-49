import random


MANUAL = 'What number is missing in the progression?'


def get_progression():

    first_num = random.randrange(1, 100)
    step = random.randrange(1, 6)
    progression = [first_num + step * i for i in range(10)]
    index = random.randrange(1, 10)
    hidden_index = progression[index]
    progression[index] = '..'
    str_progression = [str(i) for i in progression]
    progression_finish = ' '.join(str_progression)
    return progression_finish, hidden_index
