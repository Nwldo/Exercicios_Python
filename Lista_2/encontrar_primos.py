
def encontrar_primos(n):
    lista = []
    divisores = 0

    for i in range(2, n):
        for j in range(1, i+1):
            if i % j == 0:
                divisores += 1
        if divisores == 2:
            lista.append(i)
        divisores = 0

    return lista

while True:
    try:
        num = int(input("\ndigite o numero: "))
        if num > 0:
            print("Numero primo: ", encontrar_primos(num))
            break
    except:
        pass