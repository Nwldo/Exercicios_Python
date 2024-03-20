""""
10. Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior.
Se forem iguais retorna qualquer um
deles;

b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
Max.
"""
def maior(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    while True:
        numeros = []
        try:
            for i in range(4):
                num = int(input("Digite o número " + str(i+1) + ": "))
                numeros.append(num)
            break
        except:
            print("\nNúmero inválido. Digite novamente!")

    maior_numero = maior(maior(numeros[0], numeros[1]), maior(numeros[2], numeros[3]))
    print(f'\nO maior é {maior_numero}')




if __name__ == '__main__':
    main()