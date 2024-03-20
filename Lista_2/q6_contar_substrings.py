"""
Crie uma função chamada "contar_substrings" que receba uma string e uma substring
como parâmetros e retorne a quantidade de ocorrências da substring na strin
"""
def contar_substrings(string, sub_string):
    cont = 0
    for i in string:
        for j in sub_string:
            if j == i:
                cont += 1
    return cont



def main():

    while True:
        try:
            string = input('\nDigite a string: ')
            sub_string = input('\nDigite a sub_string: ')
            if string.isdigit() and sub_string.isdigit():
                raise ValueError("\nValor inválido. Digite novamente")
            else:
                print("\nA quantidade de ocorrências da substring na string: ", contar_substrings(string, sub_string))
                break
        except ValueError as e:
            print(e)



if __name__ == '__main__':
    main()