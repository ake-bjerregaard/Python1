
lista_heltal = [0, 1, 2, 3, 4, 5]

for heltal in lista_heltal:
    print(heltal)

print("------")

lista_strängar = ["Tja", "Tjena", "Hallå"]

for sträng in lista_strängar:
    print(sträng)

print("------")

lista_blandad = ["Först", 5, True, 2.5, "Sist"]

for item in lista_blandad:
    print(f'Item var av typ:{type(item)} med värdet:{item}')