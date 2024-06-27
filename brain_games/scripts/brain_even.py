#!usr/bin/env python3

from random import randint
import prompt


def play_even_game():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no"')

    i = 0

    while i < 3:
        rand_number = randint(1, 100)
        if rand_number % 2 == 0:
            correct_answer = 'yes'
        elif rand_number % 2 != 0:
            correct_answer = 'no'
        print(f'Question: {rand_number}')
        print('Your answer: ', end='')
        answer = input()
        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')

play_even_game()
