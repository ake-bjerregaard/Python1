
sträng = """ rad 1
rad 2
rad 3
"""

fileobject = open("text.txt", "a+")
fileobject.write(sträng)
fileobject.seek(0)

print("Skrivs innan", fileobject.readline())
print("Skrivs innan", fileobject.readline())
print("Skrivs innan", fileobject.readline())