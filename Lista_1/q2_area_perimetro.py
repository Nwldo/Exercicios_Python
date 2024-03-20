""""
Escreva um programa que leia o raio de um círculo e faça duas funções: uma função
chamada área que calcula e retorna a área do círculo e outra função chamada perímetro
que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r
"""


def calculaArea(r):
    a = 3.14 * (r**2)
    return a

def calculaPerimetro(r):
    p = 3.14 * 2 * r
    return p

while True:
    try:
        raio = float(input("\nDigite o raio da círculo: "))
        if raio > 0:
            print(f'\nÁrea do círculo: {calculaArea(raio):.2f}')
            print(f'\nPerímetro do círculo: {calculaPerimetro(raio):.2f}')
            break
        else:
            print('\nO valor do raio tem ser maior que zero')
    except:
        print("\nValor inválido!. Digite novamente")
