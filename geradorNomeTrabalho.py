from datetime import date
import pyperclip
import time

hoje = date.today()

codigoProf = "2021G2AN"
turma = "04J"
ano = str(hoje.year)
previaMes = str(hoje.month)
dia = str(hoje.day)
separador = "-"

def getMes():
    if len(previaMes) == 1:
        mes = ("0" + previaMes)
        return mes
    else:
        mes = previaMes
        return mes


def clipboard(codigo):
    pyperclip.copy(codigo)


def main():
    print("Digite 1 se deseja que o codigo seja copiado para seu ctrl+v, 0 para não")
    clipa = input()
    print("insira seu TIA:")
    tia = str(input())
    mes = getMes()
    codigo = codigoProf + separador + turma + separador + ano + separador + mes + separador + dia + separador + tia
    print(str(codigo))
    if clipa == "1":
        clipboard(codigo)
        print("Script ira se fechar em 5 segundos...")
        time.sleep(5)
    elif clipa == "0":
        print("Script ira se fechar em 5 segundos...")
        time.sleep(5)
        exit()



main()   