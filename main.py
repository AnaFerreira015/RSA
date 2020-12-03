from rsa import generateKey
import src.hub as hub
import src.utils as utils


if __name__ == "__main__":
    # Opção selecionada no menu
    option = hub.menu()

    if option == 1:
      generateKey()

    elif option == 2:
      print("Opção 2 escolhida")
    elif option == 3:
      print("Opção 3 escolhida")
    else:
      print("Opção inválida!")
