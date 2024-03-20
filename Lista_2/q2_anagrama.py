"""
Crie uma função chamada "verificar_anagrama" que receba duas strings como
parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as
mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário
"""
def verificar_anagrama(palavra1, palavra2):
    #palavra1 = palavra1.replace(' ', '').lower()
    #palavra2 = palavra2.replace(' ', '').lower()

    if (len(palavra1) == len(palavra2)):
        sorted_palavra1 = sorted(palavra1)
        sorted_palavra2 = sorted(palavra2)

        if sorted_palavra1 == sorted_palavra2:
            return True
        else:
            return False
    else:
        return False

def main():
    while True:
        try:
            palavra1 = input('Digite uma palavra: ').replace(' ', '').lower()
            palavra2 = input('Digite outra palvra: ').replace(' ', '').lower()

            if palavra1.isalpha() and palavra2.isalpha():
                print(verificar_anagrama(palavra1, palavra2))
                break
            else:
                raise ValueError("\nValor inválido. Digite novamente")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()
