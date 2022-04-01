#!/usr/bin/env python
from brain_games.scripts.brain_games import main as brain_games_main
import prompt
import random


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    name = brain_games_main()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for step in range(3):
        number = random.randint(1, 20)
        correct_a = is_even(number)
        print('Question: {}'.format(number))
        user_a = prompt.string('Your answer: ')
        if user_a != correct_a:
            return print(f'\'{user_a}\' is wrong answer ;(. Correct answer was \'{correct_a}\'.\nLet\'s try again, {name}!')  # noqa: E501
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
