#by Caroline Caprini

"""4) Faça uma função que determine o dobro de um número."""

import math

def readNumber():
    number = (int(input("Insira o número:")))
    return number

def doubleValue(number):

    multiply = number*2
    return multiply

def main():

    value = readNumber()
    print(doubleValue(value))

if __name__ == '__main__':
    main()