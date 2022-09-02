#!/usr/bin/env python3

import brain_games.scripts.logic
from random import randint


def even1():
    greet = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
    num1 = randint(1, 100)
    expression = num1
    if num1 % 2 == 0:
        answer = 'yes'
    if num1 % 2 != 0:
        answer = 'no'
    return (greet, expression, answer)


def main():
    brain_games.scripts.logic.engine(even1)


if __name__ == '__main__':
    main()
