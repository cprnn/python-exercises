#by Caroline Caprini

""" 2) Modularize o programa implementado no exercício 1. Ou seja, crie funções para cada
uma das ações realizadas. Quando uma ação for repetida, ao invés de escrever o
código novamente, deve-se chamar o nome da função criada que executa o código.
Crie no mínimo 3 funções e o programa principal main. """

import math

def readNumbers():
    numbers = list(map(int, input("Insira os números:").split()))
    return numbers

def calcSum(numbersList):
    calculateSum = sum(numbersList)
    print("SOMA = " + str(calculateSum))

def calcMulti(numbersList):
    calculateMulti = math.prod(numbersList)
    print("MULT = " + str(calculateMulti))

def main():

   numbers = readNumbers()
   calcSum(numbers)
   calcMulti(numbers)

if __name__ == '__main__':
    main()