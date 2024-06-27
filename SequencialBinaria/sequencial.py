import random
import time

# Função para gerar um vetor aleatório de tamanho especificado
def gerar_vetor_aleatorio(tamanho):
    vetor = [random.randint(0, tamanho * 10) for _ in range(tamanho)]
    return vetor

# Função para realizar a busca linear em um vetor
def busca_linear(vetor, alvo):
    for indice in range(len(vetor)):
        if vetor[indice] == alvo:
            return indice
    return "Não foi encontrado."

# Função principal
def main():
    tamanho = int(input("Digite o tamanho do vetor: "))
    vetor = gerar_vetor_aleatorio(tamanho)
    valor_a_buscar = int(input("Digite o valor a ser buscado: "))

    inicio_tempo = time.perf_counter()
    resultado = busca_linear(vetor, valor_a_buscar)
    fim_tempo = time.perf_counter()

    tempo_execucao = fim_tempo - inicio_tempo

    print(f"\nVetor gerado: {vetor}")
    print(f"\nResultados da Busca Linear:")
    print(f"Tamanho do vetor: {tamanho}")
    print(f"Valor buscado: {valor_a_buscar}")
    print(f"Índice encontrado: {resultado}")
    print(f"Tempo de execução: {tempo_execucao:.9f} segundos")

main()
