#stora bokstäver
for x in range(65, 91): #inklusive 65, exklusive 91
    print(chr(x))

#små bokstäver
for x in range(97, 123):
    print(chr(x))

#alla ascii tecken
for x in range(256): #range börjar på 0 om man bara har ett argument
    print(chr(x) + " " + str(x))