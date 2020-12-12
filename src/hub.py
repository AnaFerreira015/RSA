from src.utils import is_prime, mdc

def menu():
    print("")
    print("Escolha uma opção:\n")
    print("[1] Gerar chave pública")
    print("[2] Criptografar")
    print("[3] Descriptografar")
    print("[0] Sair")
    print("")

    option = -1

    while True:
        option = int(input("[+] Opção: "))

        if option in range(4):
            break
        print('[!] Opção inválida')
    return option

class Validator:
    def get_prime_input(self, varname):
        res = 0
        while True:
            res = int(input(f'[+] Valor de {varname}: '))
            if is_prime(res):
                break
            print(f'\n[!] O valor de `{varname}` precisa ser primo')

        return res

    
    def get_e_input(self, totiente: int):
        e = 0
        while True:
            e = int(input('[+] Valor de E: '))
            co_primo = mdc(totiente, e) == 1

            if co_primo and e > 1:
                break
            print('\n[!] O valor de `E` precisa ser maior que 1 e coprimo de (p-1) * (q-1)')
        return e
