
tuppel = (1, 500, 1000)

print(tuppel)

print("Första tuppel värdet: ", tuppel[0])

# tuppel[0] = 5 #går ej att göra #tuppel får inte ändra värde

tuppel2 = ("Sträng1", "Sträng2", "Sträng3", "Sträng4")

for string in tuppel2:
    print(string)

tuppel2 = tuppel

print(tuppel2)

tuppel = ("ASD", 5, True) #blandade element går bra

print(tuppel)