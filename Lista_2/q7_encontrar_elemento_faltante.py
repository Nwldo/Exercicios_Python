"""
Escreva uma função chamada "encontrar_elemento_faltante" que receba uma lista de
números de 1 a n (sendo n um número inteiro) em ordem aleatória, com um elemento
faltando, e retorne o elemento que está faltando. Ex: [4,3,1,5] = 2
"""
import random
from random import  choice, sample

def encontrar_elemento_faltante(lista):
    lista_atualizada = []
    
    for elemento in range(1, len(lista) + 1):
        if elemento not in lista:
            lista_atualizada.append(elemento)
    return  lista_atualizada


def main():
    lista = []

    numero = int(input("\nDigite o numero: "))
    for i in range(numero):
        lista.append(random.randint(1, numero))

    print(lista)
    print(f"Elemento faltante na lista lista", encontrar_elemento_faltante(lista))



if __name__ == '__main__':
    main()