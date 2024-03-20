""""
Escreva um programa para ler o número de lados de um polígono regular e a medida
do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule
e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

"""
def poligono(l, m):
    if l == 3:
        return f'TRIÂNGULO com {3*m} cm'
    elif l == 4:
        return f'QUADRADO com {m ** 2} cm'
    elif l == 5:
        return f'PENTÁGONO'
    else:
        return f'\nO número de lados está fora da faixa aceita'



def main():

    while True:
        try:
            nlados = int(input("\nDigite o número de lados entre 2 e 6: "))
            medida = float(input("\nDigite a medida do lado do poligogo: "))

            if nlados and medida > 0:
                print(poligono(nlados, medida))
                break
            else:
                print('\nOs valores têm ser maiores que zero')
        except:
            print("\nValor inválido!. Digite novamente")


if __name__ == '__main__':
    main()