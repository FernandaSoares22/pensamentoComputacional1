def calcula_h(n):
    H = 0
    sinal = 1 
    for i in range(1, n + 1):
        H += sinal * (1 / i)
        sinal *= -1 
    return H

def main():
    n = int(input("Digite o valor de N para calcular H: "))
    resultado = calcula_h(n)
    print(f"Para N = {n}, H = {resultado}")

main()
