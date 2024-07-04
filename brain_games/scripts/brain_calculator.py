#!usr/bin/env python3

from game_engine import run_game
from brain_games.games.calculator import get_calc
from brain_games.games.calculator import MANUAL


def main():
    run_game(get_calc, MANUAL)


if __name__ == '__main__':
    main()
