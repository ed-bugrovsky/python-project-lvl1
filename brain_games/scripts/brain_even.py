#!/usr/bin/env python
from brain_games.scripts.brain_games import main as brain_games_main
from brain_games.cli import defeat, victory
import prompt
import random


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    name = brain_games_main()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for step in range(3):
        number = random.randint(1, 25)
        correct_a = is_even(number)
        print('Question: {}'.format(number))
        user_a = prompt.string('Your answer: ')
        if user_a != correct_a:
            return defeat(user_a, correct_a, name)
        print('Correct!')
    return victory(name)


if __name__ == '__main__':
    main()
