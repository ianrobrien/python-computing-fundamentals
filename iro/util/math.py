# Defines mathematical functions


def is_even(integer):
    return integer % 2 == 0


def is_odd(integer):
    return not is_even(integer)


def factorial(integer):
    if integer < 0:
        raise ValueError("Factorial is undefined for a negative number")
    if integer <= 1:
        return 1
    return integer * factorial(integer - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("Cannot return negatively indexed elements")
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(n):
    if n < 0:
        raise ValueError("At least one element must be returned")
    if n == 0:
        return
    f1 = 1
    f2 = 1
    x = 0
    for i in range(0, n):
        x = f1
        f1 = f2
        f2 = x + f1
        yield x
