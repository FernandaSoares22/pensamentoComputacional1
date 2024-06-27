import random
import time

def gerar_vetor_aleatorio(tamanho):
    return [random.randint(0, tamanho * 10) for _ in range(tamanho)]

def busca_linear(vetor, alvo):
    for indice in range(len(vetor)):
        if vetor[indice] == alvo:
            return indice
    return "Não encontrado."

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
    return "Não encontrado."

def medir_tempo_pesquisa(funcao_busca, vetor, termo):
    inicio_tempo = time.perf_counter()
    indice = funcao_busca(vetor, termo)
    fim_tempo = time.perf_counter()
    return indice, fim_tempo - inicio_tempo

def testar_cenario(tamanho, termos_de_busca):
    vetor = gerar_vetor_aleatorio(tamanho)
    vetor_ordenado = sorted(vetor)
    resultados = []

    for termo in termos_de_busca:
        indice_linear, tempo_linear = medir_tempo_pesquisa(busca_linear, vetor, termo)
        indice_binaria, tempo_binaria = medir_tempo_pesquisa(busca_binaria, vetor_ordenado, termo)
        resultados.append((termo, indice_linear, tempo_linear, indice_binaria, tempo_binaria))
    
    return resultados

def main():
    tamanhos = [100, 500, 1000, 5000, 10000]
    termos_de_busca = [0, 1, 5, 10, 50, 100, 500, 1000]

    for tamanho in tamanhos:
        resultados = testar_cenario(tamanho, termos_de_busca)
        
        for resultado in resultados:
            termo, indice_linear, tempo_linear, indice_binaria, tempo_binaria = resultado
            print(f"Tamanho do vetor: {tamanho}, Termo de busca: {termo}")
            print(f"Resultado Pesquisa Linear: Índice {indice_linear}")
            print(f"Resultado Pesquisa Binária: Índice {indice_binaria}")
            print(f"Tempo Pesquisa Linear: {tempo_linear:.9f} segundos")
            print(f"Tempo Pesquisa Binária: {tempo_binaria:.9f} segundos")
            print("-----------------------")

main()
