#by Caroline Caprini

"""7) Fornecidos três valores, a, b e c, implemente uma função que retorne quantos desses
três são iguais. A reposta deve ser 2, se todos são iguais; 1, se dois são iguais ou 0, se
todos são distintos entre si."""

def readValues():
    a = int(input())
    b = int(input())
    c = int(input())

def isEqual(a,b,c):

    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0

def main():

    a, b, c = readValues()
    answer = isEqual(a,b,c)
    print(answer)

if __name__ == '__main__':
    main()