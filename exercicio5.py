#by Caroline Caprini

"""5) Faça uma função que determine o quádruplo de um número, usando a função do item
anterior."""

import exercicio4

def readNumber():
    number = (int(input("Insira o número:")))
    return number

def main():

    value = readNumber()
    print((exercicio4.doubleValue(value))*2)

if __name__ == '__main__':
    main()