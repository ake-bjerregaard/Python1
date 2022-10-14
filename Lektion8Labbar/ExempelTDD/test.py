import unittest
from projekt import student
from projekt import lärare
from projekt import person

enPerson = person.Person("Lena", "Hansson")
enElev = student.Student("Åke", "Bjerregaard")
enLärare = lärare.Lärare("Philippe", "Martinet")

assert(isinstance(enElev, student.Student))
assert(enElev.förnamn == "Åke")
assert(enElev.efternamn == "Bjerregaard")
assert(enElev.__str__() == "Åke Bjerregaard")
assert(str(enElev) == "Åke Bjerregaard")
assert(str(enLärare) == "Philippe Martinet")
assert(str(enPerson) == "Lena Hansson")
