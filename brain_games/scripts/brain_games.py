#!/usr/bin/env python
from brain_games.cli import welcome_user
import prompt


def main():
    print('Welcome to the Brain Games!')
    return welcome_user()


def engine(game, name):
    for step in range(3):
        correct_a = str(game())
        user_a = prompt.string('Your answer: ')
        if user_a != correct_a:
            return print(f'\'{user_a}\' is wrong answer ;(. Correct answer was \'{correct_a}\'.\nLet\'s try again, {name}!')  # noqa: E501
        print('Correct!')
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
