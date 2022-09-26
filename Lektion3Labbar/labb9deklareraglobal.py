x = "global sträng"

def lokala_variabler():
    global x
    y = "lokal sträng y"
    x = "lokalt tilldelat värde"
    print(f"{x} {y}")

lokala_variabler()
print("Den globala variabeln är: ", x) #globala variabelns värde har ändrats utav funktionen