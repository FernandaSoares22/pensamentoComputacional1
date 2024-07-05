def trocar_elementos(vet):
    tamanho = len(vet)
    for i in range(tamanho // 2):
        vet[i], vet[tamanho - 1 - i] = vet[tamanho - 1 - i], vet[i]
    return vet

def main():
    digite = input("Digite os elementos do vetor separados por espaço:")  
    vetor = []
    numeroAtual = ""
    for char in digite:
        if char == '-' or ('0' <= char <= '9'):
            numeroAtual += char
        else:
            if numeroAtual:
                vetor.append(int(numeroAtual))
                numeroAtual = ""
    if numeroAtual:
        vetor.append(int(numeroAtual))
    vetorTrocado = trocar_elementos(vetor)
    print("Vetor original:", vetor)
    print("Vetor após troca:", vetorTrocado)

main()
