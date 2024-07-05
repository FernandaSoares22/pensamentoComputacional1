def bubble_sort(vet, reverse):
    n = len(vet)
    if reverse  == False:
        for i in range(n):
            for j in range(0, n - i - 1):
                if vet[j] > vet[j + 1]:
                    vet[j], vet[j + 1] = vet[j + 1], vet[j]
    elif reverse == True:
        for i in range(n):
            for j in range(0, n - i - 1):
                if vet[j] < vet[j + 1]:
                    vet[j], vet[j + 1] = vet[j + 1], vet[j]

    return vet


def pesquisa_binaria(vet, item):
    vet = bubble_sort(vet, False)

    inicio = 0
    fim = len(vet) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vet[meio] == item:
            return meio
        elif vet[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def main():
    lista = [0,1,2,3,4,5,6,7,78,89]
    print(lista)
    item = int(input('Digite um valor para buscar na lista: '))
    resultado = pesquisa_binaria(lista, item)

    if resultado != -1:
        print(f'O elemento {item} foi encontrado na {resultado+1}ª posição')
    else:
        print(f'O elemento {item} não encontrado no vetor')


main()
