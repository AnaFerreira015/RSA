from rsa import RSA
import src.hub as hub

"""
Universidade Federal de Alagoas - UFAL
Programa para criptografia RSA da matéria de Matemática Discreta

Participantes:
    - Ana Ferreira
    - Frederico Guilherme
    - Lucas Tenório
    - Phyllipe Bezerra
    - Rafael Augusto
"""

if __name__ == "__main__":
    # Opção selecionada no menu
    option = hub.menu()
    rsa = RSA()

    if option == 1:
        print("\n[1] Gerar chave pública")
        rsa.generate_key()
    elif option == 2:
        print("\n[2] Criptografar")
        rsa.encrypt()
    elif option == 3:
        print("\n[3] Descriptografar")
        rsa.decrypt()
    else:
        exit(1)
