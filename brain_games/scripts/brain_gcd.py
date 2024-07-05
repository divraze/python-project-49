#!usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.gcd import get_gcd, MANUAL


def main():
    run_game(get_gcd, MANUAL)


if __name__ == '__main__':
    main()
