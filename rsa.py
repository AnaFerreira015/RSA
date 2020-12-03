from math import sqrt, floor

class rsa:
  def isPrime(n):
    # self.n = n;
    i = floor(sqrt(n))
    while i != 0:
      if i == 1:
        return True
      if n % i == 0:
        return False

      i = i - 1

  def totiente(p, q):
    return (p - 1) * (q - 1)

def mdc( a, d):
  if a == 0:
    return d

  if d == 0:
    return a

  if a < d:
    a, d = d, a

  r = a % d

  if r == 0:
    return d

  a = d
  d = r
  return mdc(a, d)

def menu():
  print('=======================')
  print('Escolha uma opção:\n1. Gerar chave pública\n2. Encriptar\n3. Desencriptar')
  print('=======================')
  option = int(input("Opção: "))
  return option

def writeFile(n, e):
  file = open('public_key.txt', 'w')
  file.write(str(n))
  file.write(' ')
  file.write(str(e))
  file.close()

def generateKey():
  p = int(input("Numero p: "))
  q = int(input("Numero q: "))

  if (rsa.isPrime(p) and rsa.isPrime(q)):
    # Tamanho do conjunto finito de valores para
    # que possamos fazer o caminho inverso ao realizado
    # para cifrar a mensagem
    n = p * q
    totiente = rsa.totiente(p, q)
    print(totiente)
    print(n)

    e = int(input("numero e: "))

    if (e > 1):
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