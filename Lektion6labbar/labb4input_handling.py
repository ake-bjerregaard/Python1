
print("Skriv in din ålder")
inmatning = input()
try:
    ålder = int(inmatning)
    print("Din ålder är ", ålder)
except ValueError as err:
    print(err)
print("Här är slutet på programmet")