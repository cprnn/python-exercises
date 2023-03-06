#by Caroline Caprini

"""6) Faça uma função que, dado um total de segundos, calcule o total de horas, minutos e
segundos."""

def readSeconds():
    seconds = (int(input("Insira o número:")))
    return seconds

def convert(seconds):

    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    return hours, minutes, seconds


def main():

    value = readSeconds()
    hours, minutes, seconds = convert(value)
    print(f"{value} segundos equivalem a {hours} horas, {minutes} minutos e {seconds} segundos.")

if __name__ == '__main__':
    main()