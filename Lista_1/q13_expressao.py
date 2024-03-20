""""
Escreva uma função que recebe por parâmetro um valor inteiro e
positivo N e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
"""

def expressao(n):
    exp = (1 + (1/2) + (1/3) + (1/4) + (1/5) + 1/n)
    return exp

def main():
    while True:
        try:
            numero = int(input("\nDigite um número inteiro e positivo: "))
            if numero >= 0:
                print(f"O valor da expressão é: {expressao(numero):.2f}")
                break
            else:
                print("\nO número precisa ser positivo e diferente de zero.")
        except:
            print("\nNúmero inválido. Digite novamente!")


if __name__ == '__main__':
    main()