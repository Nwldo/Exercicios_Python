"""
Escreva uma função chamada "contar_caracteres" que receba uma string como
parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string
e os valores são a quantidade de ocorrências de cada caractere.
"""




def main():

    ocorrencia = {}
    frase = input("\nDigite o texto: ").replace(' ', '').lower()
    for caracter in frase:
        if 'a' <= caracter <= 'z':  # só se for letra
            ocorrencia[caracter] = ocorrencia[caracter] + 1 if caracter in ocorrencia else 1

    print(ocorrencia)

if __name__ == '__main__':
    main()