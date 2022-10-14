import unittest
from rest import heltalsdivision

assert(callable(heltalsdivision))
assert(heltalsdivision(4, 3) == 1)
assert(heltalsdivision(1.5, 1) == 1)
assert(heltalsdivision(12, 3) == 4)