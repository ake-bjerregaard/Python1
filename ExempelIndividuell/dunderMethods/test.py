import unittest
from djurklasser import *

apan = Apa()
elefant = Elefant()

assert(isinstance(apan, Apa))
assert(isinstance(apan, Djur))
assert(type(apan) is Apa)
assert(str(apan) == "Apan hoppar och äter banan")
assert(apan.__str__() == "Apan hoppar och äter banan")
assert(str(elefant) == "Dricker vatten")
assert(isinstance(elefant, Elefant))
assert(isinstance(elefant, Djur))