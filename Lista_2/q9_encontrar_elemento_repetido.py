"""
Escreva uma função chamada "encontrar_elemento_repetido" que receba uma lista de
números como parâmetro e retorne o elemento que se repete mais vezes na lista.
"""
import random


def encontrar_elemento_repetido(lista):
    quantidade_ocorrencias = 0
    item_com_maior_ocorrencia = 0
    soma_lista = {}

    for item in lista:
        if item not in soma_lista:
            soma_lista[item] = 0

        soma_lista[item] += 1

    for item in soma_lista:
        if soma_lista[item] > quantidade_ocorrencias:
            quantidade_ocorrencias = soma_lista[item]
            item_com_maior_ocorrencia = item

    return f'O item com maior ocorrência é {item_com_maior_ocorrencia} ' \
           f'com {quantidade_ocorrencias} ocorrências.'

def main():
    lista = []
    while True:
        try:
            numero = int(input("\nDigite um número inteiro: "))

            for i in range(numero):
                lista.append(random.randint(1, numero))
            print(lista)

            if numero > 0:
                print(encontrar_elemento_repetido(lista))
                break
            else:
                print("\nO número precisa ser positivo e diferente de zero.")
        except ValueError:
            print("\nNúmero inválido. Digite novamente!")


if __name__ == '__main__':
    main()