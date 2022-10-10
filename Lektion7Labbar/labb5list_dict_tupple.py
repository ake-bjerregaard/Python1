
lista = [5, 14, 2.5, "hejsan"]

dictionary = {"nyckel1" : "värde1", "nyckel2" : "värde2"}
print(dictionary["nyckel1"])
print(dictionary.get("nyckel2"))
print(dictionary.get("finns inte")) #ger inget error
print(dictionary.keys())
print(dictionary.values())

tuppel = ("tjohej", True, 512.05)


def returnera_punkt():
    return (250, 50)

koordinat = returnera_punkt()
print(type(koordinat))

def for_loop_över_samlingsklass(samling): #samling = collection
    for x in samling:
        print(x)

print("----")
for_loop_över_samlingsklass(lista)
print("----")
for_loop_över_samlingsklass(dictionary)
print("----")
for_loop_över_samlingsklass(tuppel)

for key, value in dictionary.items():
    print(f'Key: {key} Value: {value}')
