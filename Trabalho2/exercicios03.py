def filtra_numeros(numeros):
    resultado = []
    for numero in numeros:
        if 1000 <= numero <= 9999:
            parte1 = numero // 100
            parte2 = numero % 100
            print(f"Número: {numero}")
            print(f"Parte 1: {parte1}")
            print(f"Parte 2: {parte2}")
            if (parte1 + parte2) ** 2 == numero:
                resultado.append(numero)
                print(f"({parte1} + {parte2}) ** 2 = {numero} - Satisfaz a propriedade!\n")
            else:
                print(f"({parte1} + {parte2}) ** 2 = {(parte1 + parte2) ** 2} - Não satisfaz a propriedade.\n")
    return resultado

def main():
    digite = input("Digite uma lista de números de 4 dígitos, separados por espaço: ")
    numeros = []
    numeroAtual = ""
    for char in digite:
        if '0' <= char <= '9':
            numeroAtual += char
        elif numeroAtual:
            numeros.append(int(numeroAtual))
            numeroAtual = ""
    if numeroAtual:
        numeros.append(int(numeroAtual))
    resultado = filtra_numeros(numeros)
    if resultado:
        print("Os números que satisfazem a propriedade são:", resultado)
    else:
        print("Nenhum número satisfaz a propriedade.")

main()
