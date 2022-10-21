dictionary = {'nyckel1': 'värde1', 'nyckel2': 'värde2'}

for x in dictionary:
    print(x)

for nyckel, värde in dictionary.items():
    print("Nyckeln var " + nyckel + " och värdet var " + värde)

for x in dictionary.values():
    print("Värdet var " + x)