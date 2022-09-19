from kodtecken import programming_signs
from test_methods import print_correct
from test_methods import simple_write_with_sign

signs = programming_signs()

Sign.swedish = True

for k, v in signs.items():
    simple_write_with_sign(v)
    
Sign.swedish = False

for k, v in signs.items():
    simple_write_with_sign(v)

# print_correct("Hello world!", "Write a print function with that writes \"Hello world!\" exactly!")