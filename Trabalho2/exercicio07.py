def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    inverso = texto[::-1]
    if texto == inverso:
        return True
    else:
        return False


def main():
    frase = input('Digite uma frase: ').strip()
    resultado = eh_palindromo(frase)

    if resultado:
        print(f'A palavra/frase "{frase}" é palíndromo.')
    else:
        print(f'A palavra/frase "{frase}" não é palíndromo.')


main()
