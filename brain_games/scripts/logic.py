#!/usr/bin/env python3

import prompt


def engine(logika):
    print('Welcome to the Brain Games!')
    [greet, expression, answer] = logika()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{greet}')
    counter = 0
    while counter < 3:
        [greet, expression, answer] = logika()
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            counter = counter + 1
            print('Correct!')
        if user_answer != str(answer):
            counter = 0
            print(f'''\'{user_answer}\' is wrong answer ;(.
Correct answer was \'{answer}\'.''')
            print(f'Let\'s try again, {name}!')
            return counter
    print(f'Congratulations, {name}!')
