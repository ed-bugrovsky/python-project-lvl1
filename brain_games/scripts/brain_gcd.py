#!/usr/bin/env python
from brain_games.scripts.brain_games import main as general_main, engine
import random


def gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    case = '{} {}'.format(number1, number2)
    print('Question: {}'.format(case))
    divisor = abs(number1 - number2)
    while divisor != 1:
        if number1 % divisor == 0 and number2 % divisor == 0:
            return divisor
        else:
            divisor -= 1
    return 1


def main():
    name = general_main()
    print('Find the greatest common divisor of given numbers.')
    return engine(gcd, name)


if __name__ == '__main__':
    main()
