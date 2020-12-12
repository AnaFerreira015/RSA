from math import sqrt, floor
from src.hub import Validator
from src.utils import find_congruence
from src.mdchar import *
from src.utils import mdc

class RSA:
    # @staticmethod
    def totiente(self, p, q):
        return (p - 1) * (q - 1)

    def write_file(self, content, name):
        file = open(f"{name}.txt", "w")
        file.write(content)
        file.close()

    def read_encrypted(self):
        file = open("encrypted_message.txt", "r")
        file_content = file.read()
        file.close()
        return file_content
    
    # Pega o conteúdo da mensagem em string e transforma em um array
    def str_to_array(self, string):
        # Retira os colchetes e os espaços da string original
        comma_divided_content = string.replace("]", "").replace("[", "").replace(" ", "")
        return comma_divided_content.split(",")

    def generate_key(self):
        validator = Validator()

        p = validator.get_prime_input('P')
        q = validator.get_prime_input('Q')

        # Tamanho do conjunto finito de valores para
        # que possamos fazer o caminho inverso ao realizado
        # para cifrar a mensagem

        n = p * q

        while (n < 26):
            print('P * Q precisa ser maior que 26')
            p = validator.get_prime_input('P')
            q = validator.get_prime_input('Q')
            n = p * q
        totiente = self.totiente(p, q)

        e = validator.get_e_input(totiente)

        while(mdc(n, e) != 1):
            print('[!] `N` e `E` precisam ser coprimos!')
            e = validator.get_e_input(totiente)
        self.write_file(f"{n} {e}", "public_key")
    
    def encrypt(self):
        message = input("[+] Digite a mensagem a ser criptografada: ")

        n = int(input("[+] Valor de N: "))
        e = int(input("[+] Valor de E: "))

        encrypted = []
        for char in message:
            ascii_code = md_ord(char)
            encrypted_char = pow(ascii_code, e, n)

            encrypted.append(encrypted_char)
        
        self.write_file(str(encrypted), "encrypted_message")

    def decrypt(self):
        p = int(input("[+] Valor de P: "))
        q = int(input("[+] Valor de Q: "))
        e = int(input("[+] Valor de E: "))

        encrypted_content = self.read_encrypted()
        parsed_array = self.str_to_array(encrypted_content)
        phiN = (p - 1) * (q - 1)
        n = p * q
        d = find_congruence(e, 1, phiN)

        decrypted_message = ""
        for ascii_code in parsed_array:
            ascii_int = int(ascii_code)
            decrypted_code = pow(ascii_int, d, n)

            # if decrypted_code <= 1:
            #     decrypted_code += n

            decrypted_message += md_chr(decrypted_code)

        print(decrypted_message)


