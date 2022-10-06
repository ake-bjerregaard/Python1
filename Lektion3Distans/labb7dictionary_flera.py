
dictionary = {
    "nyckel1" : "värde1",
    "nyckel2" : "värde2",
    "nyckel3" : 543,
    "nyckel4" : 0.4,
    "nyckel5" : True,
    "baranåt" : "något olikt"
}

print(dictionary["nyckel4"])

print(dictionary["baranåt"])

print("------ Skriv ut hela listan: ------")
for x in dictionary:
    print(x)