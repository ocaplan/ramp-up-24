def iterative_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def recursive_factorial(num):
    if num == 1:
        return 1
    return num * recursive_factorial(num - 1)


def factorial(num):
    if num < 0:
        return print("-1")
    print("Iterative Calculation: " + str(iterative_factorial(num)))
    print("Recursive Calculation: " + str(recursive_factorial(num)))