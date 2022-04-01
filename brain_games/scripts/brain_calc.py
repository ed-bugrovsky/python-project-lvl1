#!/usr/bin/env python
from brain_games.scripts.brain_games import main as general_main, engine
import random


def calc():
    operators = ('+', '-', '*')
    number1 = random.randint(1, 25)
    number2 = random.randint(1, 25)
    operator = random.randint(0, 2)
    case = '{} {} {}'.format(number1, operators[operator], number2)
    print('Question: {}'.format(case))
    return eval(case)


def main():
    name = general_main()
    print('What is the result of the expression?')
    return engine(calc, name)


if __name__ == '__main__':
    main()
