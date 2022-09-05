#!/usr/bin/env python3

import brain_games.scripts.logic
from random import randint


def prime5():
    greet = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
    num1 = randint(1, 100)
    expression = str(num1)
    if num1 < 2:
        answer = 'no'
    elif num1 == 2:
        answer = 'yes'
    else:
        for i in range(2, num1):
            if num1 % i == 0:
                answer = 'no'
                return (greet, expression, answer)
        answer = 'yes'
        return (greet, expression, answer)


def main():
    brain_games.scripts.logic.engine(prime5)


if __name__ == '__main__':
    main()
