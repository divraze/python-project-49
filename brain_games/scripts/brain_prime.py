#!usr/bin/env python3

from random import randrange
import prompt


def is_prime(n):

    if n <= 1:
        return 'no'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'




def play_prime_game():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0

    while i < 3:
        
        n = randrange(1, 101)
        correct_answer = is_prime(n)

        print(f'Question: {n}')
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
    play_prime_game()


if __name__ == '__main__':
    main()
