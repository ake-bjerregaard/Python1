# from sys import argv

# [print(arg) for arg in argv]


def min_egen_funktion_med_returvärde(arg1):
    return type(arg1)

lista = ["Tjo", 5, 1.0, True]

typlista = [min_egen_funktion_med_returvärde(objekt) for objekt in lista]

print(typlista)