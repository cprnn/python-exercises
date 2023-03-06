#by Carol Caprini

""" 1) Faça um programa que leia 4 números e mostre a soma e a multiplicação dos
mesmos
 """

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    sum = a + b + c + d
    mult = a * b * c * d   

    print("SOMA = " + str(sum))
    print("MULT = " + str(mult))

if __name__ == '__main__':
    main()