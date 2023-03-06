#by Caroline Caprini

""" 3) Pesquise sobre funções da biblioteca math (matemáticas) e utilize duas delas em
exemplos. https://docs.python.org/3/library/math.html """

import math

def readNumber():
    number = int(input("Insira o número:"))
    return number

""" 
Operação 1 - cálculo de logarítmo na base 2
math.log2(x)
Return the base-2 logarithm of x. This is usually more accurate than log(x, 2)."""

def calcLog2(number):
    calculateLog = math.log(number)
    print("Log de x na base 2 = " + str(calculateLog))

""" 
Operação 2 - cálculo de raíz quadrada
math.sqrt(x)
Return the square root of x. """

def calcSqrt(number):
    calculateSqrt = math.sqrt(number)
    print("A raíz quadrada de x é = " + str(calculateSqrt))

def main():

   n = readNumber()
   calcLog2(n)
   calcSqrt(n)

if __name__ == '__main__':
    main()