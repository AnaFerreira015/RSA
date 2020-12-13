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
