"""
Crie uma função chamada "remover_vogais" que receba uma string como parâmetro e
retorne uma nova string sem as vogais.
"""
def remover_vogais(string):
    nova_string = ''

    for caracter  in string:
        if caracter not in "aeiou":
            nova_string = nova_string + '' + caracter

    return nova_string

def main():

    while True:
        try:
            string= input("Digite uma letra: ").lower().strip()

            if string.isdigit():
                raise ValueError("\nValor inválido. Digite novamente")
            else:
                print("\nNova string sem as vogasi: ", remover_vogais(string))
                break
        except ValueError as e:
            print(e)



if __name__ == '__main__':
    main()