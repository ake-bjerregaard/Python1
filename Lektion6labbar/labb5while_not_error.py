success = False

while not success:
    print("Skriv in din ålder")
    inmatning = input()
    try:
        ålder = int(inmatning)
        print("Din ålder är ", ålder)
        success = True
    except ValueError as err:
        print("Du angav inte ett heltal")
        # print(err)
print("Här är slutet på programmet")