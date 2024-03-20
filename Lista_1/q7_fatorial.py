""""
7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial,
sabemos que N! depende de (N-1)!; este por
sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se
que fatorial de 1 é igual a 1 mesmo. Utilize
uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial,
do tipo inteiro, e retorna o fatorial deste
número, também do tipo inteiro.

"""

def e_fatorial(n):
    fat = 1
    for i in range(1, n + 1): #Se n for 0! ou 1! será impresso o valor 1
        fat *= i
    return fat

while True:
    try:
        num = int(input("Informe o número: "))

        if num >= 0:
            print(f'\nO fatorial de {num} é: {e_fatorial(num)}')
            break
        else:
            print('\nO valor tem ser maior que zero')
    except:
        print("\nValor inválido!. Digite novamente") # For digitado string por exemplo