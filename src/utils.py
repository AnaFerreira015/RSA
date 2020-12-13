from math import sqrt, floor
from random import randint


def fermat(n: int) -> bool:
    """Função para checar se um dado número é primo
    Args:
        n (int): O número a ser testado
    Returns:
        [bool]: Se é primo ou não
    """
    if n == 1:
        return False

    roof = floor(sqrt(n))
    return len([1 for i in range(1, roof + 1) if n % i == 0]) == 1


def miller_rabin(n, k=5) -> bool:
    """Função de Miller–Rabin para checar se um dado número é primo

    Args:
        n (int): O número a ser testado

    Returns:
        [bool]: Se é primo ou não
    """

    # Se n for menor do que 2 retorna falso, já que nenhum número <2 é primo
    if n < 2:
        return False
    """ Para todos os números primos contidos no array, checa se n mod p é 0.
    Caso seja, então p divide n e então retornamos se n é igual a p
    """
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d / 2
    for i in range(k):
        x = pow(randint(2, n - 1), d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime(n: int) -> bool:
    if len(str(n)) > 13:
        return miller_rabin(n)
    else:
        return fermat(n)


def mdc(a: int, d: int) -> int:
    """Função para calcular o mdc entre dois números

    Args:
        a (int): Um número inteiro qualquer
        d (int): Um número inteiro qualquer

    Returns:
        int: O MDC entre os dois números
    """
    if a == 0:
        return d

    if d == 0:
        return a

    if a < d:
        a, d = d, a

    r = a % d

    if r == 0:
        return d

    return mdc(d, r)


def coefficients(a, d, div, num1=None, num2=None):
    if div == []:
        num1 = a
        num2 = d

    if d == 0:
        return [1, 0]
    if a == 0:
        return [0, 1]

    r = a % d
    s = int(a / d)
    div.append(s)

    if r == 0:
        if len(div) == 1:
            s = 1
            t = -1
        elif len(div) == 2:
            s = 1
            t = -(num1 - 1) / num2

        else:
            i = 0
            div.pop()
            div.reverse()
            j = len(div) - 1
            c = []

            while i <= j:
                if i == 0:
                    c.append(div[i])
                    i = i + 1

                elif i == 1:
                    c.append(div[i] * c[i - 1] + 1)
                    i = i + 1

                else:
                    c.append(div[i] * c[i - 1] + c[i - 2])
                    i = i + 1

            if len(div) % 2 == 0:
                s = -abs(c[-2])
                t = abs(c[-1])

            else:
                s = abs(c[-2])
                t = -abs(c[-1])

        return [int(s), int(t)]

    return coefficients(d, r, div, num1, num2)


def find_inverse(num1: int, num2: int):
    """Função para calcular o inverso de um número mod outro

    Args:
        num1 (int): Um número inteiro qualquer
        num2 (int): Um número inteiro qualquer

    Returns:
        int: O inverso de [num1] mod [num2]
    """
    if num2 > num1:
        [t, s] = coefficients(num2, num1, [])
    else:
        [s, t] = coefficients(num1, num2, [])

    return floor(int(s))


def find_congruence(a: int, b: int, m: int) -> int:
    """Função para encontrar um número que multiplicado por a é congruente b mod m

    Args:
        a (int): Um inteiro qualquer
        b (int): Um inteiro qualquer
        m (int): Um inteiro qualquer

    Returns:
        int: O valor que multiplicado por [a] é congruente [b] mod [m]
    """
    if b == 0:
        return 0

    d = mdc(a, m)

    if m == 0 or b % d != 0:
        return "Não tem solução"

    a = int(a / d)
    b = int(b / d)
    m = int(m / d)

    s = find_inverse(a, m)

    result = s * b

    return result % m
