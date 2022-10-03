
#enkel klass utan argument med 2 variabler i varje instans
#self är instansen självt
class EnKlass:
    def __init__(self):
        self.variabelnamn = "Hello"
        self.variabelnamn2 = "World!"


enInstans = EnKlass()

print(enInstans.variabelnamn)
print(enInstans.variabelnamn2)

