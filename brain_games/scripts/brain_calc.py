#!/usr/bin/env python3

import brain_games.scripts.logic
from random import randint
from random import choice


def calc2():
    greet = 'What is the result of the expression?'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    oper = ['+', '-', '*']
    oper = choice(oper)
    answer = str(num1) + str(oper) + str(num2)
    answer = eval(answer)
    expression = str(num1) + ' ' + str(oper) + ' ' + str(num2)
    return (greet, expression, answer)


def main():
    brain_games.scripts.logic.engine(calc2)


if __name__ == '__main__':
    main()
