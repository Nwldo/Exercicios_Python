""""
Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.
"""

def contar_numeros(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

def main():
    while True:
        try:
            numero = int(input("\nDigite um número inteiro e positivo: "))
            if numero >= 0:
                print("O somatório desse valor é:", contar_numeros(numero))
                break
            else:
                print("\nO número precisa ser positivo e diferente de zero.")
        except ValueError:
            print("\nNúmero inválido. Digite novamente!")


if __name__ == '__main__':
    main()