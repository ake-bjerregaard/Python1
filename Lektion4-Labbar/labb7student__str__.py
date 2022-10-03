#här en klass som kräver ett argument för att skapas
class Student:
    
    def __init__(self, argument_förnamn, argument_efternamn):
        self.förnamn = argument_förnamn
        self.efternamn = argument_efternamn

    def __str__(self):
        return f"{self.förnamn} {self.efternamn}"

enElev = Student("Maria", "Johansen")
enAnnanElev = Student("Jonas", "Ekblom")

print(enElev)
print(enAnnanElev)