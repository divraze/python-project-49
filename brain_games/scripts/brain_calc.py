#!usr/bin/env python3

from random import randint
from random import choice
import prompt


def play_calc_game():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What is the result of the expression?')

    i = 0

    while i < 3:
        num_1 = randint(1, 10)
        num_2 = randint(1, 10)
        signs = choice(['+', '-', '*'])
        expression = f'{num_1} {signs} {num_2}'
        correct_answer = eval(expression)

        print(f'Question: {expression}')
        print('Your answer: ', end='')
        answer = int(input())

        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    play_calc_game()


if __name__ == '__main__':
    main()
