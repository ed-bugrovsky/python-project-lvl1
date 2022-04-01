#!/usr/bin/env python
from brain_games.scripts.brain_games import main as general_main, engine
import random


def even():
    case = random.randint(1, 25)
    print('Question: {}'.format(case))
    return 'yes' if case % 2 == 0 else 'no'


def main():
    name = general_main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return engine(even, name)


if __name__ == '__main__':
    main()
