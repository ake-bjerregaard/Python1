def funktion1():
    print(">>Början Funktion1")
    funktion2()
    print(">>Slutet Funktion1")

def funktion2():
    print(">>>>     Början Funktion2")
    funktion3()
    print(">>>>     Slutet Funktion2")

def funktion3():
    print(">>>>>>         Funktion3")

funktion1()