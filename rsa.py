from math import sqrt, floor
from src.utils import is_prime, mdc, find_congruence


class rsa:
    # @staticmethod
    def totiente(p, q):
        return (p - 1) * (q - 1)

    def write_file(content, name):
        file = open(f"{name}.txt", "w")
        file.write(content)
        file.close()

    def read_encrypted():
        file = open("encrypted_message.txt", "r")
        file_content = file.read()
        file.close()
        return file_content
    
    # Pega o conteúdo da mensagem em string e transforma em um array
    def str_to_array(string):
        # Retira os colchetes e os espaços da string original
        comma_divided_content = string.replace("]", "").replace("[", "").replace(" ", "")
        return comma_divided_content.split(",")

    def generate_key(self):
        p = int(input("Numero p: "))
        q = int(input("Numero q: "))

        if is_prime(p) and is_prime(q):
            # Tamanho do conjunto finito de valores para
            # que possamos fazer o caminho inverso ao realizado
            # para cifrar a mensagem
            n = p * q
            totiente = self.totiente(p, q)
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
                self.write_file(f"{n} {e}", "public_key")
            else:
                print("`e` precisa ser maior do que 1")
    
    def encrypt(self):
        message = input("Digite a mensagem a ser encriptada: ")

        n = int(input("Digite o n: "))
        e = int(input("Digite o e: "))

        encrypted = []
        for char in message:
            ascii_code = ord(char)
            encrypted_char = pow(ascii_code, e, n)

            encrypted.append(encrypted_char)
        
        self.write_file(str(encrypted), "encrypted_message")

    def decrypt(self):
        p = int(input("Numero p: "))
        q = int(input("Numero q: "))
        e = int(input("numero e: "))

        encrypted_content = self.read_encrypted()
        parsed_array = self.str_to_array(encrypted_content)
        phiN = (p - 1) * (q - 1)
        n = p * q
        d = find_congruence(e, 1, phiN)

        decrypted_message = ""
        for ascii_code in parsed_array:
            ascii_int = int(ascii_code)
            decrypted_code = pow(ascii_int, d, n)

            decrypted_message += chr(decrypted_code)

        print(decrypted_message)


