#!/usr/bin/env python3

import brain_games.scripts.logic
from random import randint


def gcd3():
    greet = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    expression = str(num1) + ' ' + str(num2)
    while (num1 != 0) and (num2 != 0):
        if num1 >= num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
        answer = num1 + num2
    return (greet, expression, answer)


def main():
    brain_games.scripts.logic.engine(gcd3)


if __name__ == '__main__':
    main()
