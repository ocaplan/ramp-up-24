from math import factorial


def factorial_of_factorials(num):
    if num == 1:
        return num
    return factorial(num) * factorial_of_factorials(num - 1)
