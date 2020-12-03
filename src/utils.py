from math import sqrt, floor


def is_prime(n):
    roof = floor(sqrt(n))
    return len([1 for i in range(1, roof + 1) if n % i == 0]) == 1


def mdc(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
