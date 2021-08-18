from datetime import date

hoje = date.today()

codigoProf = "2021G2AN"
turma = "04J"
ano = str(hoje.year)
previaMes = str(hoje.month)
dia = str(hoje.day)
separador = "-"

def main():
    print("insira seu TIA:")
    tia = str(input())
    mes = getMes()
    print(codigoProf + separador + turma + separador + ano + separador + mes + separador + dia + separador + tia)


def getMes():
    if len(previaMes) == 1:
        mes = ("0" + previaMes)
        return mes


main()   