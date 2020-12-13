from src.utils import MathUtils, FileUtils, Validator
from src.mdchar import *

validator = Validator()
mathUtils = MathUtils()
fileUtils = FileUtils()

class RSA:
    def generate_key(self):
        """Gera a chave pública pegando todos os inputs do usuário"""

        [p, q] = validator.get_p_and_q_input()

        # Tamanho do conjunto finito de valores para
        # que possamos fazer o caminho inverso ao realizado
        # para cifrar a mensagem

        n = p * q

        while n <= 26:
            print("[!] P * Q precisa ser maior que 26")
            p = validator.get_prime_input("P")
            q = validator.get_prime_input("Q")
            n = p * q
        totiente = mathUtils.totiente(p, q)

        e = validator.get_e_input(totiente)


        self.write_file(f"{n} {e}", "public_key")

    def encrypt(self):
        message = input("[+] Digite a mensagem a ser criptografada: ")

        n = int(input("[+] Valor de N: "))
        e = int(input("[+] Valor de E: "))

        encrypted = []
        for char in message:
            char_code = md_ord(char)
            encrypted_char = pow(char_code, e, n)

            encrypted.append(encrypted_char)

        fileUtils.write_file(str(encrypted), "encrypted_message")

    def decrypt(self):
        """Função para descriptografar uma determinada mensagem"""
        p = int(input("[+] Valor de P: "))
        q = int(input("[+] Valor de Q: "))
        e = int(input("[+] Valor de E: "))

        encrypted_content = fileUtils.read_encrypted()
        parsed_array = fileUtils.str_to_array(encrypted_content)
        phiN = (p - 1) * (q - 1)
        n = p * q
        d = mathUtils.find_congruence(e, 1, phiN)

        decrypted_message = ""
        for char_code in parsed_array:
            char_int = int(char_code)
            decrypted_code = pow(char_int, d, n)

            decrypted_message += md_chr(decrypted_code)

        print(decrypted_message)
