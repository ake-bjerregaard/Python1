def function(**kwargs): #keywordarguments
    print(kwargs)
    print(type(kwargs)) #blir ett dictionary
    for i in kwargs:
      print (i,kwargs[i])

function(a=1, b=2, c=3, d=4)

print("--------------")

def function_med_argument_också(arg1, **dictionary_argument):
    print(arg1)
    print(dictionary_argument)

function_med_argument_också("Tjena", a=1, b="tjohej", c=False)

