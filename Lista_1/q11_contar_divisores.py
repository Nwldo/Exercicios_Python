""""
Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o número de divisores desse valor.
"""

def contar_divisores(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores

def main():
    while True:
        try:
            numero = int(input("\nDigite um número inteiro e positivo: "))
            if numero >= 0:
                print("O número de divisores é:", contar_divisores(numero))
                break
            else:
                print("\nO número precisa ser positivo e diferente de zero.")
        except ValueError:
            print("\nNúmero inválido. Digite novamente!")


if __name__ == '__main__':
    main()