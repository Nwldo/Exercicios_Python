""""
Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro
se ele for par e falso se for ímpar.

"""
def parImpar(num):
    if num % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        num = int(input("Digite o numero: "))
        if isinstance(num, int):
            print(f'\nO número {num} é par? {parImpar(num)}')
            break
    except:
        print("\nNúmero inválido!. Digite novamente")

