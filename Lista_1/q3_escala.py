""""
Escreva um programa para ler uma temperatura em graus Fahrenheit.
Faça uma função chamada celsius para calcular e retornar
o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5
"""
def converter(f):
    c = ((f-32)/9)*5
    return c

while True:
    try:
        fah = float(input("\nConverter fahrenheit para Celsius: "))
        print(f'\nTemperatura em Celsius é: {converter(fah):.2f}')
        break
    except:
        print("\nTemperatura inválida!. Digite novamente")