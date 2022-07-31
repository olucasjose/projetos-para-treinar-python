import os

off = 'n'

while (off == 'n'):
    fator1 = int(input(''))
    operacao = (input(''))
    fator2 = int(input(''))
    if operacao == "a":
        print(fator1 + fator2)
    if operacao == "s":
        print(fator1 - fator2)
    if operacao == "m":
        print(fator1 * fator2)
    if operacao == "d":
        print(fator1 / fator2)
    if operacao == "p":
        print(int(fator1 * fator2 / 100))
    if operacao == "pr":
        print(float(fator1 * 100 / fator2))
    off = input('Encerrar calculadora? (s/n/nc) ')
    if off == 'nc':
        os.system("clear")
