#!usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.prime import get_prime, MANUAL


def main():
    run_game(get_prime, MANUAL)


if __name__ == '__main__':
    main()
