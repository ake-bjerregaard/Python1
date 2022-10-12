

def upphöjt(tal):
    return tal*tal


lista = [1, 2, 3, 4]

resultat = map(upphöjt, lista)
print(type(resultat))
print(list(resultat))



