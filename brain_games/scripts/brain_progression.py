#!/usr/bin/env python3

import brain_games.scripts.logic
from random import randint


def progression4():
    greet = 'What number is missing in the progression?'
    step = randint(1, 10)
    start = randint(1, 100)
    amount = randint(5, 15)
    end = start + step * amount
    change = randint(1, amount - 1)
    expression = list(range(start, end, step))
    answer = expression[change]
    expression[change] = '..'
    expression = '[%s]' % ' ' .join(map(str, expression))
    expression = expression[1:-1]
    return (greet, expression, answer)


def main():
    brain_games.scripts.logic.engine(progression4)


if __name__ == '__main__':
    main()
