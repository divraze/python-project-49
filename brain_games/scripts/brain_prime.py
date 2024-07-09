#!usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.prime import get_question_and_answer, MANUAL


def main():
    run_game(get_question_and_answer, MANUAL)


if __name__ == '__main__':
    main()
