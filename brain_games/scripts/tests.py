#!usr/bin/env python3

import prompt

def game_process():

    name = prompt.string(
f'''Welcome to the Brain Games!
May I have your name? '''
)
    print(f'Hello, {name}!')










def main():
    game_process()


if __name__ == '__main__':
    main()
