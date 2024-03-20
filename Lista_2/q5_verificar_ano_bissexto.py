"""
Escreva uma função chamada "verificar_ano_bissexto" que receba um número inteiro
como parâmetro e retorne True se o ano for bissexto, e False caso contrário. Um ano é
bissexto se for divisível por 4, mas não divisível por 100, exceto se for divisível por 400.
"""

from datetime import date

def ano_bissexto(ano):
    if ano == 0:
        ano = date.today().year
    if (ano % 4 ==0 and ano % 100 !=0) or (ano % 400 ==0):
        #print('\nO ano {} é BiSSEXTO'.format(ano))
        return True
    else:
        #print('\nO ano {} não é BISSEXTO'.format(ano))
        return False

def main():

    while True:
        try:
            ano = int(input('\nDigite o ano ou 0 para o ano atual: '))
            if ano >= 0:
                print("\nO número de divisores é:", ano_bissexto(ano))
                break
            else:
                print("\nO número precisa ser positivo e diferente de zero.")
        except ValueError:
            print("\nNúmero inválido. Digite novamente!")



if __name__ == '__main__':
    main()