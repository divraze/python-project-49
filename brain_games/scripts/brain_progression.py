#!usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.progression import get_progression
from brain_games.games.progression import MANUAL


def main():
    run_game(get_progression, MANUAL)


if __name__ == '__main__':
    main()
