def funktion1(arg1):
    funktion2(arg1)

def funktion2(argument1):
    funktion3(argument1)

def funktion3(a1):
    a1 = "något annat"

variabel = "nåt"
funktion1(variabel)
print(variabel)