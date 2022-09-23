from time import sleep

# print("Det är bara text", input())

variabelnamn = "lite text"


def väntaOchReturneraSträng():
    sleep(5)
    return "Den här strängen"

print("Nu kör vi")
print("Det är bara text", väntaOchReturneraSträng(), " print ")
print("Det här kommer senare")


