from math import sqrt, floor
import re

class MathUtils:
    def totiente(self, p, q):
        """Função totiente de Euler ou Função phi, mede a capacidade de quebra de um número

        Args:
            p (int): Um número primo
            q (int): Um número primo

        Returns:
            int: A quantidade de números inteiros que são menores do que, ou iguais a, p e q
        """
        return (p - 1) * (q - 1)

    def is_prime(self, n: int) -> bool:
        """Função para checar se um dado número é primo
        Args:
            n (int): O número a ser testado
        Returns:
            [bool]: Se é primo ou não
        """
        if (n < 2):
            return False

        roof = floor(sqrt(n))

        for i in range(2, roof + 1):
            if n % i == 0:
                return False

        return True


    def mdc(self, a: int, d: int) -> int:
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

        return self.mdc(d, r)


    def coefficients(self, a, d, div, num1=None, num2=None):
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

        return self.coefficients(d, r, div, num1, num2)


    def find_inverse(self, num1: int, num2: int):
        """Função para calcular o inverso de um número mod outro

        Args:
            num1 (int): Um número inteiro qualquer
            num2 (int): Um número inteiro qualquer

        Returns:
            int: O inverso de [num1] mod [num2]
        """
        if num2 > num1:
            [t, s] = self.coefficients(num2, num1, [])
        else:
            [s, t] = self.coefficients(num1, num2, [])

        return floor(int(s))


    def find_congruence(self, a: int, b: int, m: int) -> int:
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

        d = self.mdc(a, m)

        if m == 0 or b % d != 0:
            return "Não tem solução"

        a = int(a / d)
        b = int(b / d)
        m = int(m / d)

        s = self.find_inverse(a, m)

        result = s * b

        return result % m

class FileUtils:
    def write_file(self, content, name):
        """Escreve um determinado conteúdo em um arquivo

        Args:
            content (string): O conteúdo que irá ser escrito no arquivo
            name (string): O nome do arquivo
        """
        file = open(f"{name}.txt", "w")
        file.write(content)
        file.close()

    def read_encrypted(self):
        """Lê o arquivo `encrypted_message.txt`

        Returns:
            string: O conteúdo do arquivo lido
        """

        try:
            file = open("encrypted_message.txt", "r")
            file_content = file.read()
            file.close()
            return file_content
        except:
            raise RuntimeError("O arquivo encrypted_message.txt não existe.")

    def format_input(self, text):
        clear = re.sub('[\]\[\n,]', ' ', text)
        return re.sub(' +', ' ', clear).strip()

    def str_to_array(self, string):
        """Pega o conteúdo da mensagem em string e transforma em um array

        Args:
            string (string): O conteúdo da mensagem

        Returns:
            [list(string)]: Um array do conteúdo da mensagem
        """

        formatted_message = self.format_input(string)


        return formatted_message.split(" ")

mathUtils = MathUtils()

class Validator:
    """Validator é uma classe específica para encapsular validações de input"""

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
            if mathUtils.is_prime(res):
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
            co_primo = mathUtils.mdc(totiente, e) == 1

            if co_primo and e > 1 and e < totiente:
                break
            print(
                "\n[!] O valor de `E` precisa ser maior que 1, menor que o totiente e também coprimo de (p-1) * (q-1)"
            )
        return e