#här en klass som kräver ett argument för att skapas
class Student:
    
    def __init__(self, argument_namn):
        self.namn = argument_namn

enElev = Student("Meriem")
enAnnanElev = Student("Jonas")

print(enElev.namn)
print(enAnnanElev.namn)