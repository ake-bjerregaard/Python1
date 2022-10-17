import unittest
from addition_func import addition

assert(callable(addition))
assert(addition(5, 7) == 12)
assert(addition(2, 7) == 9)
assert(addition(-2, -5) == -7)
