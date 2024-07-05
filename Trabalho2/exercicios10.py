def filtrar(texto, lista_negativa):
    texto_filtrado = ''
    
    i = 0
    dentro_palavra = False
    palavra_atual = ''
    
    while i < len(texto):
        if texto[i].isspace() or texto[i] in [',', '.', ':', ';', '!', '?']:
            if dentro_palavra:
                if palavra_atual.lower() in lista_negativa:
                    texto_filtrado += '*' * len(palavra_atual)
                else:
                    texto_filtrado += palavra_atual
                dentro_palavra = False
                palavra_atual = ''
            
            texto_filtrado += texto[i]
        else:
            dentro_palavra = True
            palavra_atual += texto[i]
        
        i += 1
    
    return texto_filtrado

texto = "Este é um exemplo de texto para filtrar palavras proibidas."
lista_negativa = ['exemplo', 'palavras']

texto_filtrado = filtrar(texto, lista_negativa)
print(texto_filtrado)
