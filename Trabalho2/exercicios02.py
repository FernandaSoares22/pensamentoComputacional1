def obter_numeros_paridade(n, c):
    resultado = []
    if c == 'p':
        for num in range(1, n):
            if num % 2 == 0:
                resultado.append(num)
    elif c == 'i':
        for num in range(1, n):
            if num % 2 != 0:
                resultado.append(num)
    return resultado

def main():
    n = int(input("Digite o valor do limite superior (N): "))
    c = input("Digite 'p' para pares ou 'i' para ímpares: ")
    resultado = obter_numeros_paridade(n, c)
    if resultado:
        print("Os valores gerados são:", resultado)
    else:
        print("Caractere inválido. Por favor, digite 'p' para pares ou 'i' para ímpares.")

main()
