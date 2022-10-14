import unittest
from matte import upphöjt

assert(callable(upphöjt))
assert(upphöjt(3, 2) == 9)
assert(upphöjt(4, 3) == 64)
assert(upphöjt(5, 6) == 15625)
assert(upphöjt(1, 0) == 1)
assert(upphöjt(0, 0) == 1)
assert(upphöjt(2, -1) == 0.5)
assert(upphöjt(2, -2) == 0.25)
