def intercala(s1, s2):
    s3 = ''
    if len(s1) > len(s2):
        maior = s1
    else:
        maior = s2

    for c in range(len(maior)):
        if c < len(s1):
            s3 += s1[c]
        if c < len(s2):
            s3 += s2[c]
    return s3

def desintercala(s3, s2):
    s1 = ''
    cont_tam_s2 = 0

    for i in range(len(s3)):
        if cont_tam_s2 < len(s2) and s3[i] == s2[cont_tam_s2]:
            cont_tam_s2 += 1
        else:
            s1 += s3[i]
    return s1

def main():

    primeira_palavra = input('Digite uma palavra: ')
    segunda_palavra = input('Digite outra palavra: ')
    terceira_palavra = intercala(primeira_palavra, segunda_palavra)

    print('='*30)
    print(f'''s1 = {primeira_palavra}
s2 = {segunda_palavra}
s3 = {terceira_palavra}''')

    primeira_denovo = desintercala(terceira_palavra, segunda_palavra)
    print('='*30)
    print(f'''s3 = {terceira_palavra}
s2 = {segunda_palavra}
s1_denovo = {primeira_denovo}''')
    print('='*30)

main()
