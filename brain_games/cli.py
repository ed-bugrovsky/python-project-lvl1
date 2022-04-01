import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def defeat(user_a, correct_a, name):
    return print(f'\'{user_a}\' is wrong answer ;(. Correct answer was \'{correct_a}\'.\nLet\'s try again, {name}!')  # noqa: E501


def victory(name):
    return print(f'Congratulations, {name}!')
