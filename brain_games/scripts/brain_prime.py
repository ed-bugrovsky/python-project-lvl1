#!/usr/bin/env python
from brain_games.scripts.brain_games import main as general_main, engine
import random


def prime():
    case = random.randint(1, 100)
    counter = 0
    for i in range(2, case // 2 + 1):
        if case % i == 0:
            counter += 1
    print('Question: {}'.format(case))
    return 'yes' if counter == 0 else 'no'


def main():
    name = general_main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return engine(prime, name)


if __name__ == '__main__':
    main()
