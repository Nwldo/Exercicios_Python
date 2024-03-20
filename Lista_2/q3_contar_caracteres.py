"""
Escreva uma função chamada "contar_caracteres" que receba uma string como
parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string
e os valores são a quantidade de ocorrências de cada caractere.
"""

def contar_caracteres(str):
    qdt_caracteres = {}
    for caracter in str:
        if 'a' <= caracter <= 'z':  # só se for letra
            if caracter in qdt_caracteres:
                qdt_caracteres[caracter] = qdt_caracteres[caracter] + 1
            else:
                qdt_caracteres[caracter] = 1

    return qdt_caracteres

def main():

    frase = input("\nDigite o texto: ").replace(' ', '').lower()
    print(contar_caracteres(frase))


if __name__ == '__main__':
    main()