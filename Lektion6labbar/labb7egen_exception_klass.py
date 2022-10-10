class IngenSträngException(Exception):
    
    def __init__(self, message="Det var ingen sträng"):
        self.message = message

class TomSträngException(Exception):

    def __init__(self, message="Strängen ska inte tom"):
        self.message = message

class Student:

    def __init__(self, namn):
        # if not namn.isinstance(str):
        if type(namn) is not str:
            raise IngenSträngException
        if namn == "":
            raise TomSträngException
        self.namn = namn
        

nyElev = Student("Johanna")
try:    
    ytterliggareElev = Student("")
    annanElev = Student(None)
    print(nyElev.namn)
    print(annanElev.namn)
except IngenSträngException as err:
    print(err.message)
except TomSträngException as err:    
    print("Studenten får inte ha ett tomt namn")
    
print("Slutet av programmet")

