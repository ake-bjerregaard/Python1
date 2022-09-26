x = "global sträng"

def lokala_variabler():
    y = "lokal sträng y"
    x = "lokal sträng x"
    print(f"{x} {y}")

lokala_variabler()
print("Den globala variabeln är: ", x)