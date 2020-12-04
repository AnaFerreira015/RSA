from math import sqrt, floor
from src.utils import is_prime, mdc, find_congruence


class rsa:
    # @staticmethod
    def totiente(p, q):
        return (p - 1) * (q - 1)

    def writeFile(content, name):
        file = open(f"{name}.txt", "w")
        file.write(content)
        file.close()

    def readEncrypted():
        file = open("encrypted_message.txt", "r")
        file_content = file.read()
        file.close()
        return file_content
    
    # Pega o conteúdo da mensagem em string e transforma em um array
    def parseStrToArr(string):
        # Retira os colchetes e os espaços da string original
        comma_divided_content = string.replace("]", "").replace("[", "").replace(" ", "")
        return comma_divided_content.split(",")

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
                rsa.writeFile(f"{n} {e}", "public_key")
            else:
                print("`e` precisa ser maior do que 1")
    
    def encrypt():
        message = input("Digite a mensagem a ser encriptada: ")

        n = int(input("Digite o n: "))
        e = int(input("Digite o e: "))

        encrypted = []
        for char in message:
            ascii_code = ord(char)
            encrypted_char = (ascii_code ** e) % n

            encrypted.append(encrypted_char)
        
        rsa.writeFile(str(encrypted), "encrypted_message")

    def decrypt():
        p = int(input("Numero p: "))
        q = int(input("Numero q: "))
        e = int(input("numero e: "))

        encrypted_content = rsa.readEncrypted()
        parsed_array = rsa.parseStrToArr(encrypted_content)
        print('parsed_array ', parsed_array)
        phiN = (p - 1) * (q - 1)
        n = p * q
        print('n ', n)
        print('phiN ', phiN)
        d = find_congruence(e, 1, phiN)
        print('d ', d)

        decrypted_message = ""
        for ascii_code in parsed_array:
            ascii_int = int(ascii_code)
            print('ascii_int ', ascii_int)
            decrypted_code = (ascii_int ** d) % n
            print('decrypted_code ', decrypted_code)

            decrypted_message += chr(decrypted_code)

        print(decrypted_message)


