lista3 = [0, 1, 2]
lista4 = [3, 4, 5]
lista5 = lista3 + lista4
print(lista5)


for x in lista3:
    print(x)

print("----------")

for idx, x in enumerate(lista3):
    resultat = lista3[idx] + lista4[idx]
    print(f"""{lista3[idx]} + {lista4[idx]} = {resultat}""")
