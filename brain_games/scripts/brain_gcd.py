#!usr/bin/env python3

from random import randint
import prompt


def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    if num_1 != 0:
        return num_1
    return num_2


def play_gcd():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Find the greatest common divisor of given numbers.')

    i = 0

    while i < 3:
        num_1 = randint(1, 10)
        num_2 = randint(1, 10)
        correct_answer = gcd(num_1, num_2)

        print(f'Question: {num_1, num_2}')
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
    play_gcd()


if __name__ == '__main__':
    main()
