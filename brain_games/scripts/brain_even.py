#!/usr/bin/env python3

import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer \"yes\" if the number is even, otherwise answer \"no\".')
    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and number % 2 == 0) or (answer == 'no' and number % 2 != 0):
            counter = counter + 1
            print('Correct!')
        if answer == 'yes' and number % 2 != 0:
            counter = 0
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f'Let\'s try again, {name}!')
        if answer == 'no' and number % 2 == 0:
            counter = 0
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f'Let\'s try again, {name}!')
        if answer != 'no' and answer != 'yes' and number % 2 == 0:
            counter = 0
            print(f'{answer} is wrong answer ;(. Correct answer was \'yes\'.')
            print(f'Let\'s try again, {name}!')
        if answer != 'no' and answer != 'yes' and number % 2 != 0:
            counter = 0
            print(f'{answer} is wrong answer ;(. Correct answer was \'no\'.')
            print(f'Let\'s try again, {name}!')
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
