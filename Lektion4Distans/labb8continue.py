

lista = [1, 5, 4, -1, 5, 2, 10]

for x in lista:
    if(x == -1):
        continue #vi hoppar över att skriva -1, vi avbryter den här iterationen av loopen och fortsätter nästa varv
    print(x)

print("--------")

i = 0
while(i < 10):

    if i == 5:
        while(True):
            break
    else:
        print(i)
    i += 1
