#!/usr/bin/env python
from brain_games.scripts.brain_games import main as general_main, engine
import random


def progression():
    step = random.randint(1, 10)
    number = random.randint(1, 100)
    case = list()
    for i in range(random.randint(5, 15)):
        case.append(str(number))
        number += step
    missing = random.randint(1, len(case) - 2)
    answer = case[missing]
    case[missing] = '..'
    print('Question: {}'.format(' '.join(case)))
    return answer


def main():
    name = general_main()
    print('What number is missing in the progression?')
    return engine(progression, name)


if __name__ == '__main__':
    main()
