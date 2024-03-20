"""
Crie uma função chamada encontrar_primos_gemeos que receba um número inteiro
n como parâmetro e retorne uma lista contendo todos os pares de números primos
gêmeos menores que n. Os números primos gêmeos são dois números primos
consecutivos que diferem em 2.
"""

def encontrar_primos(n):
    primos = []
    primos_gemeos = []
    divisores = 0

    for i in range(2, n):
        for j in range(1, i+1):
            if i % j == 0:
                divisores += 1
        if divisores == 2:
            primos.append(i)
        divisores = 0

    for i in range(0, len(primos), 2):
        primos_gemeos.append(primos[i])

    return primos_gemeos

while True:
    try:
        num = int(input("\ndigite o numero: "))
        if num > 0:
            print("Numero primo: ", encontrar_primos(num))
            break
    except:
        print("\nValor inválido. Digite novamente")





