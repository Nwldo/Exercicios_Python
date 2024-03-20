""""
8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere
somente se ele for igual a S ou N.
Se o caractere não for nem S nem N, a função imprime a mensagem 'Caractere inválido. Digite novamente'.
Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo
na tela.
O programa deve ficar lendo os números até o usuário responder 'N' à
pergunta se ele deseja continuar ou não.
"""
def caracter(char):
    if char == 'S' or char == 'N':
        return char
    else:
        return f'\nCaractere inválido.Digite novamente'


while True:
    try:
        num = float(input('\nDigite um numero: '))
        if num > 0:
            cubo = num ** 3
            print(f'\nO cubo do {num} é: {cubo}')

            op = str(input('Deseja continuar (S/N): ')).upper()
            print(caracter(op))
            if caracter(op) == 'N':
                break
        else:
            print("Numero deve ser maior que zero")

    except:
        print('\nValor inválido. Digite novamente!')
