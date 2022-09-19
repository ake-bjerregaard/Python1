from kodtecken import programming_signs
from kodtecken import Sign
from test_methods import print_correct
from test_methods import simple_write_with_sign_and_text

signs = programming_signs()

Sign.swedish = True

for k, v in signs.items():
    simple_write_with_sign_and_text(v, "Skriv ")
    
Sign.swedish = False

for k, v in signs.items():
    simple_write_with_sign_and_text(v, "Write ")
    
while(username == ""):
    print("Skriv ditt förnamn. Avsluta med enterslag:")
    username = input()
    
while(usersurname == ""):
    print("Skriv ditt efternamn. Avsluta med enterslag:")
    usersurname = input()

# print_correct("Hello world!", "Write a print function with that writes \"Hello world!\" exactly!")