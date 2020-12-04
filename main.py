from rsa import rsa
import src.hub as hub
import src.utils as utils


if __name__ == "__main__":
    # Opção selecionada no menu
    option = hub.menu()

    if option == 1:
      rsa.generateKey()

    elif option == 2:
      # print("Opção 2 escolhida")
      rsa.encrypt()
    elif option == 3:
      # print("Opção 3 escolhida")
      rsa.decrypt()
    else:
      print("Opção inválida!")
      # rsa.decrypt

