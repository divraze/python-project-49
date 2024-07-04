#!usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.even import get_even
from brain_games.games.even import MANUAL


def main():
    run_game(get_even, MANUAL)


if __name__ == '__main__':
    main()
