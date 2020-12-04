from math import sqrt, floor


def is_prime(n):
    roof = floor(sqrt(n))
    return len([1 for i in range(1, roof + 1) if n % i == 0]) == 1


def mdc(a, d):
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


def coefficients(a, d, div, num1 = None, num2 = None):
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
                    i = i+1

                elif i == 1:
                    c.append(div[i] * c[i - 1] + 1)
                    i = i+1

                else:
                    c.append(div[i] * c[i - 1] + c[i - 2])
                    i = i + 1

            if len(div)%2 == 0:
                s = -abs(c[-2])
                t = abs(c[-1])

            else:
                s = abs(c[-2])
                t = -abs(c[-1])
                
        return [int(s), int(t)]

    return coefficients(d, r, div, num1, num2)


def find_inverse(num1, num2):
    if num2 > num1:
        [t, s] = coefficients(num2, num1, [])
    else:
        [s, t] = coefficients(num1, num2, [])

    return floor(int(s))


def find_congruence(a, b, m):
    if b == 0:
        return 0

    d = mdc(a, m)

    if m == 0 or b % d != 0:
        return "Não tem solução"

    a = int(a / d)
    b = int(b /d)
    m = int(m / d)

    s = find_inverse(a, m)

    result = s * b

    return result % m