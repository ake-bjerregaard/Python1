import random #importerar hela modulen
from random import choice #importerar funktionen choice
from random import random as ettannatnamn #importerar vi funktionen med ett namn som jag väljer


print(random.random()) #skriver ut ett slumpmässigt flyttal mellena 0 och 1

lista = ["Tjabba", "Tjena", "Hallå"]
print(choice(lista))  #skriver ut ett slumpmässigt element ur listan

random.choice(lista)

print(ettannatnamn()) #samma funktion som random.random() men vi har satt ett eget namn på funktionen