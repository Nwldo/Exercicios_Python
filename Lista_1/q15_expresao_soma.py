""""
15. Escreva uma função que recebe por parâmetro um valor inteiro
e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
"""
def soma(n):
    result = 0
    for t in range(1,n+1):
        numerador = t**2 + 1
        denominador = t + 3
        result += numerador / denominador
    return result

while True:
    try:
        num = int(input("\nDigite a quantidade de termos: "))
        if num <=0:
            print("\nValor negativo ou igual a zero, Digite novamente")
        else:
            print(f"A soma é {soma(num):.2f}")
            break
    except:
        print("\nValor inválido. Digite novamente!")
