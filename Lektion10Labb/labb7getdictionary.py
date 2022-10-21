
dictionary = {'nyckel1': 'värde1', 'nyckel2': 'värde2'}

värde =  dictionary.get("nyckel1")

print(värde)

finns_ej = dictionary.get("nåt som inte finns")

print(finns_ej)

if(dictionary.get("nyckel2")):
    print("nyckeln fanns i dictionary")

if(dictionary.get("finns ej")):
    print("nyckeln fanns i dictionary")
else:
    print("nyckeln finns inte")
