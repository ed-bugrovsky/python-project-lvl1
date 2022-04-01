#!/usr/bin/env python
from brain_games.scripts.brain_games import main as brain_games_main
from brain_games.cli import defeat, victory
import prompt
import random


def calculator(number1, number2, operator):
    operators = ('+', '-', '*')
    output = '{} {} {}'.format(number1, operators[operator], number2)
    print('Question: {}'.format(output))
    return eval(output)


def main():
    name = brain_games_main()
    print('What is the result of the expression?')
    for step in range(3):
        number1 = random.randint(1, 25)
        number2 = random.randint(1, 25)
        operator = random.randint(0, 2)
        correct_a = calculator(number1, number2, operator)
        user_a = prompt.string('Your answer: ')
        if user_a != str(correct_a):
            return defeat(user_a, correct_a, name)
        print('Correct!')
    return victory(name)


if __name__ == '__main__':
    main()
