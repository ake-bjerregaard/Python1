class IngenSträngException(Exception):
    
    def __init__(self, message="Det var ingen sträng"):
        self.message = message

class Student:

    def __init__(self, namn):
        # if not namn.isinstance(str):
        if type(namn) is not str:
            raise IngenSträngException
        self.namn = namn
        

nyElev = Student("Johanna")
try: 
    annanElev = Student(None)
    print(nyElev.namn)
    print(annanElev.namn)
except IngenSträngException as err:
    print(err.message)
    
print("Slutet av programmet")

