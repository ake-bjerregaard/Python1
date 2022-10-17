import unittest
from multiplication_func import multiplikation


assert(callable(multiplikation))
assert(multiplikation(2, 7) == 14)
assert(multiplikation(2, 2) == 4)
assert(multiplikation(-5, -5) == 25)
