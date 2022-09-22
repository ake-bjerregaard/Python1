import sys
# sys.path.insert(0,'..') #kinda ugly way to move back and import
from assignmentpackage import programming_signs
from assignmentpackage import Sign
from assignmentpackage import print_correct
from assignmentpackage import simple_write_with_sign_and_text
from assignmentpackage import WholeHistory

signs = programming_signs()

Sign.swedish = True

for k, v in signs.items():
    simple_write_with_sign_and_text(v, "Skriv ")
    
Sign.swedish = False

for k, v in signs.items():
    simple_write_with_sign_and_text(v, "Write ")
    
#print("Hello world!")

#print(variabler)

#matematematiska formler + - * / #med och utan variabler.

#exempel for loopar som ska skriva #med range

#if satser

printExempel = '''Givet variablerna nedan. Sätt ihop det till denna sträng:
Hejdå!
sträng1 = "Hej "
sträng2 = "då!"

'''
# sträng1 + sträng2







username = ""    
while(username == ""):
    print("Skriv ditt förnamn. Avsluta med enterslag:")
    username = input()
    
userlastname = ""
while(userlastname == ""):
    print("Skriv ditt efternamn. Avsluta med enterslag:")
    userlastname = input()
    
assignment1string = username + " " + userlastname

 
log_file = open("assignment1.testoop","w")
log_file.write(assignment1string) 
for x in WholeHistory.wholeHistory:
    log_file.write(x)
log_file.close()