
lista = ["Hej", "tjabba"]

tuppel = (5, lista, True)

print(tuppel)

lista[1] = "då" #detta går bra då tuppel bara har en referense till listan

print(tuppel)

tuppel2 = ("nåt", "nåt2")

tuppel3 = tuppel + tuppel2

print(tuppel3)