# # from sys import argv
# # script, user_name = argv



# prompt = '> '

# print("Write your name")
# # likes = input()
# # print(likes)
# something = eval("4")
# print(something)
 
# prstr = "print('Hi')"
# wut = eval(prstr)
# print(wut)

import io
import sys



def print_correct(answer, instructionText):
    correct = False
    while(not correct):
        try:
            print(instructionText)
            capturedOutput = io.StringIO();
            userInput = input()
            sys.stdout = capturedOutput
            exec(userInput)
            sys.stdout = sys.__stdout__
            correct = capturedOutput.getvalue() == answer + "\n"
        except KeyboardInterrupt:
            sys.exit()
        except BaseException as err:
            sys.stdout = sys.__stdout__
            print(err)
    print("You passed the test")        
    
def handle_exec(userInput):
    try:
        capturedOutput = io.StringIO();
        sys.stdout = capturedOutput
        exec(userInput)
        sys.stdout = sys.__stdout__
        return capturedOutput
    except KeyboardInterrupt:
        sys.exit()
    except BaseException as err:
        sys.stdout = sys.__stdout__
        print(err)
        return capturedOutput

def print_correct2(answer, instructionText):
    correct = False
    while(not correct):
        print(instructionText)
        userInput = input()
        capturedOutput = handle_exec(userInput)
        correct = capturedOutput.getvalue() == answer + "\n"
    print("You passed the test")    
    
def multiple_choice_print(rightAnswer, wrongAnswers, instructionText):
    print(instructionText)
    
    
    
def multiple_choice(rightAnswer, wrongAnswers, instructionText):
    multiple_choice_print(rightAnswer, wrongAnswers, instructionText)
    
import time    
    
def simple_write(rightAnswer, instructionText):
    correct = False
    while(not correct):
        print(instructionText + rightAnswer)
        userInput = input()
        correct = userInput == rightAnswer
    print("Bra jobbat!\n")
    time.sleep(0.7)
    
def simple_write_with_sign(sign):
    correct = False
    rightAnswer = sign.sign
    while(not correct):
        print("Skriv " + str(sign) + ": " + sign.sign)
        userInput = input()
        correct = userInput == rightAnswer
    print("Bra jobbat!\n")
    time.sleep(0.7)
    
def simple_write_with_sign_and_text(sign, text):
    correct = False
    rightAnswer = sign.sign
    while(not correct):
        print(text + str(sign) + ": " + sign.sign)
        userInput = input()
        correct = userInput == rightAnswer
    print("Bra jobbat!\n")
    time.sleep(0.7)
        
    
# simple_write("(", "Skriv startparantes: ");
# simple_write(")", "Skriv slutparantes: ");
# simple_write("\"", "Skriv citattecken: ");

    
# multiple_choice("Hello world!", ["asss", "SDASD", "sdasda"], "What does print(\"Hello world!\" write in the console?")
    

# print_correct2("Hello world!", "Write a print function with that writes \"Hello world!\" exactly!")

#cheat code
# sys.stdout=sys.__stdout__;print('print("Hello World!")');print("You passed the test!");import os;os._exit(0)
    
    # https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention
    # modules (filenames) should have short, all-lowercase names, and they can contain underscores;
# packages (directories) should have short, all-lowercase names, preferably without underscores;
# classes should use the CapWords convention.
#type(1)

#vars(someclass) #dumps information about it
#operator immutable mutable