def imprime_gradual(palavra):
    tamanho = len(palavra)
    meio = tamanho // 2
    
    for i in range(meio, -1, -1):
        print(palavra[i:tamanho - i])

palavra = "SONHO"
imprime_gradual(palavra)
