""""
4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre.
Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva a média semestral
e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação).
"""

def media_notas(n1, n2):
    media = (n1 + n2) / 2
    return media


while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = media_notas(nota1, nota2)

        if nota1 and nota2 > 0:
            if media > 6:
                print(f'\nMédia semestral {media}: PARABÉNS! Você foi aprovado')
                break
            else:
                print(f'\nMédia semestral {media} Você foi reprovado :)')
                break
        else:
            print('\nOs valores têm ser maiores que zero')
    except:
        print("\nNota inválida!. Digite novamente")