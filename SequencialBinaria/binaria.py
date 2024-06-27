import random
import time

def gerar_lista_ordenada(tamanho):
    return sorted([random.randint(0, tamanho * 10) for _ in range(tamanho)])

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return "Não foi encontrado."

def main():
    tamanho = int(input("Digite o tamanho da lista ordenada: "))
    lista = gerar_lista_ordenada(tamanho)
    valor_a_buscar = int(input("Digite o valor a ser buscado: "))

    inicio_tempo = time.perf_counter()
    resultado = busca_binaria(lista, valor_a_buscar)
    fim_tempo = time.perf_counter()

    tempo_execucao = fim_tempo - inicio_tempo

    print(f"\nLista gerada: {lista}")
    print(f"\nResultados da Busca Binária:")
    print(f"Tamanho da lista: {tamanho}")
    print(f"Valor buscado: {valor_a_buscar}")
    print(f"Índice encontrado: {resultado}")
    print(f"Tempo de execução: {tempo_execucao:.9f} segundos")

main()
