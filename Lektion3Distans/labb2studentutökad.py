#här en klass som kräver ett argument för att skapas
class Person:
    
    def __init__(self, argument_förnamn, argument_efternamn, argument_personnr):
        self.förnamn = argument_förnamn
        self.efternamn = argument_efternamn
        self.personnr = argument_personnr


    def __str__(self):
        return f"{self.förnamn} {self.efternamn} {self.personnr}"

class Lärare(Person):
    
    def __init__(self, argument_förnamn, argument_efternamn, argument_personnr, lön):
        super().__init__(argument_förnamn, argument_efternamn, argument_personnr)
        self.lön = lön

    def __str__(self):
        return f'{super().__str__()} {self.lön}'


class Student(Person):

    def __init__(self, argument_förnamn, argument_efternamn, argument_personnr, betyg):
        super().__init__(argument_förnamn, argument_efternamn, argument_personnr)
        self.betyg = betyg
    
    def __str__(self):
        return f'{super().__str__()} {self.betyg}'

enElev = Student("Maria", "Johansen", "521001-0631", "VG")
enAnnanElev = Student("Jonas", "Ekblom", "800501-6512", "G")

lärare = Lärare("Åke", "Bjerregaard", "761001-5678", 30000)


print(enElev)
print(enAnnanElev)
print(lärare)