""""
14. Escreva uma função que recebe por parâmetro um valor inteiro e
positivo N e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
"""
def soma(n):
    result = 0
    for t in range(1,n+1):
        numerador = 1
        denominador = e_fatorial(t)
        result += numerador / denominador
    return result

def e_fatorial(n):
    fat = 1
    for i in range(1, n + 1): #Se n for 0! ou 1! será impresso o valor 1
        fat *= i
    return fat

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



