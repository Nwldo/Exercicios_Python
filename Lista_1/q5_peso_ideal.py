""""
5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso
ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima).
"""

def pesoIdeal(s,alt):
    if s == 1:
        ph = (62.1 * alt) - 44.7
        return ph
    elif s == 2:
        pm = (72.7 * alt) - 58
        return pm


while True:
    try:
        sexo = int(input("\nDigite 1 feminino / 2 masculino: "))
        altura = float(input("\nDigite a altura: "))

        if sexo and altura > 0:
            if (1 <= sexo <= 2) and (0.60 < altura <= 2.30):
                print(f'\nPeso ideal: {pesoIdeal(sexo, altura):.2f}')
                break
            else:
                print('\nOs valores estão fora da faixa aceita')
        else:
            print('\nOs valores têm ser maiores que zero')
    except:
        print("\nValor inválido!. Digite novamente")