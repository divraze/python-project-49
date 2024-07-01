#!usr/bin/env python3

from random import randrange
import prompt


def progression_game_logic():

    first_num = randrange(1, 100)
    step = randrange(1, 6)
    progression = [first_num + step * i for i in range(10)]
    index = randrange(1, 10)
    hidden_index = progression[index]
    progression[index] = '..'
    str_progression = [str(i) for i in progression]
    progression_finish = ' '.join(str_progression)

    return progression_finish, hidden_index




def play_progression_game():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What number is missing in the progression?')

    i = 0

    while i < 3:
        progression_finish, hidden_index = progression_game_logic()

        correct_answer = str(hidden_index)

        print(f'Question: {progression_finish}')
        print('Your answer: ', end='')
        answer = str(input())

        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')













def main():
    play_progression_game()


if __name__ == '__main__':
    main()
