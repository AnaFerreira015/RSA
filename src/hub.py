from src.utils import is_prime, mdc


def menu():
    """Função para exibir o menu principal

    Returns:
        int: A opção escolhida, de 0 a 3
    """
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
        print("[!] Opção inválida")
    return option


class Validator:
    """Validator é uma classe específica para encapsular validações de input"""
    def get_p_and_q_input(self):
        """Função para requerir um input do e P e do Q

        Returns:
            [list(int)]: Retorna uma lista com p e q entrados pelo usuário, respectivamente
        """

        p = self.get_prime_input("P")
        q = self.get_prime_input("Q")
        while p == q:
            print(f"\n[!] O valor de `P` e `Q` precisam ser diferentes")
            p = self.get_prime_input("P")
            q = self.get_prime_input("Q")

        return [p, q]

    def get_prime_input(self, varname):
        """Função para requerir um input de um número primo

        Args:
            varname (string): Nome da variável a ser entrada pelo usuário

        Returns:
            [int]: Retorna o número primo entrado pelo usuário
        """
        res = 0
        while True:
            res = int(input(f"[+] Valor de {varname}: "))
            if is_prime(res):
                break
            print(f"\n[!] O valor de `{varname}` precisa ser primo")

        return res

    def get_e_input(self, totiente: int):
        """Função para requerir o valor de E

        Args:
            totiente (int): O valor da função totiente

        Returns:
            [int]: O valor de e, que é coprimo do totiente
        """
        e = 0
        while True:
            e = int(input("[+] Valor de E: "))
            co_primo = mdc(totiente, e) == 1

            if co_primo and e > 1 and e < totiente:
                break
            print(
                "\n[!] O valor de `E` precisa ser maior que 1, menor que o totiente e também coprimo de (p-1) * (q-1)"
            )
        return e
