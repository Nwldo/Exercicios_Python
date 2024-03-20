"""
Escreva uma função chamada "verificar_quadrado_perfeito" que receba um número
inteiro como parâmetro e retorne True se o número for um quadrado perfeito, e False
caso contrário. Um número inteiro é considerado um quadrado perfeito quando ele é o
resultado da multiplicação de um número inteiro por ele mesmo. Em outras palavras, um
número inteiro "n" é um quadrado perfeito se existir um número inteiro "m" tal que "n =
m * m". Por exemplo, os números 4, 9, 16 e 25 são quadrados perfeitos, pois podem ser
obtidos pela multiplicação de um número inteiro por ele mesmo: 4 = 2 * 2; 9 = 3 * 3; 16 =
4 * 4; 25 = 5 * 5.
Obs: não utilizar a função raiz quadrada isqrt()
"""

def verificar_quadrado_perfeito(n):

    raizQ = int(n ** (1 / 2))

    if (raizQ ** 2) == n:
        return True
    else:
        return False

def main():
    
    while True:
        try:
            numero = int(input("\nDigite um número inteiro: "))

            if numero > 0:
                print(f'O número é um quadrado perfeito? {verificar_quadrado_perfeito(numero)}')
                break
            else:
                print("\nO número precisa ser positivo e diferente de zero.")
        except ValueError:
            print("\nNúmero inválido. Digite novamente!")


if __name__ == '__main__':
    main()