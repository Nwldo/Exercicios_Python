
def primos(n):
    lista = []
    divisores = 0

    for i in range(2, n):
        if n % i == 0:
            divisores += 1
    if divisores == 0:
        return n
    else:
        return f'não é primo'

while True:
    try:
        num = int(input("\ndigite o numero: "))
        if num > 0:
            print("Numero primo: ", (num))a
            break
    except:
        pass