def md_ord(char):
    upper_char = char.upper()
    # Se o char for um espaço, então retorna 28
    if ord(upper_char) == 32:
        return 28

    char_ord = ord(upper_char) - 63
    # Se o ord do char que é para ser convertido for entre [2, 27]
    if char_ord >= 2 and char_ord <= 27:
        return char_ord
    raise RuntimeError(f"Caractere [{char}] não é válido")


def md_chr(code):
    if code == 28:
        return " "
    if code >= 2 and code <= 27:
        return chr(code + 63)
    raise RuntimeError(f"Código [{code}] não é um char válido")
