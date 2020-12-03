from math import sqrt, floor
from src.utils import is_prime, mdc


class rsa:
    @staticmethod
    def totiente(p, q):
        return (p - 1) * (q - 1)


def writeFile(n, e):
    file = open("public_key.txt", "w")
    file.write(str(n))
    file.write(" ")
    file.write(str(e))
    file.close()


def generateKey():
    p = int(input("Numero p: "))
    q = int(input("Numero q: "))

    if is_prime(p) and is_prime(q):
        # Tamanho do conjunto finito de valores para
        # que possamos fazer o caminho inverso ao realizado
        # para cifrar a mensagem
        n = p * q
        totiente = rsa.totiente(p, q)
        print(totiente)
        print(n)

        e = int(input("numero e: "))

        if e > 1:
            # quantidade de co-primos de um numero que
            # são menores que ele mesmo
            coPrimos = mdc(totiente, e)
            while (coPrimos != 1) or (e <= 1):
                e = int(input("numero e: "))
                coPrimos = mdc(totiente, e)
            print(coPrimos)
            # Escreve a quantidade de co-primos e o número `e` em um arquivo
            writeFile(n, e)
        else:
            print("`e` precisa ser maior do que 1")
