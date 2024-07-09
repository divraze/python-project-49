import random


MANUAL = 'What number is missing in the progression?'


def get_progression():
    first_num = random.randrange(1, 100)
    step = random.randrange(1, 6)
    progression = [first_num + step * i for i in range(10)]
    return progression


def get_question_and_answer():
    progression = get_progression()
    index = random.randrange(1, 10)
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join([str(i) for i in progression])
    return question, answer
