
set = {5, 2, 1, 9}

print(set)

set2 = set.union({7,5,2, 500})

print(set2)

print(500 in set2) #är 500 i set2? # ja, det är sant
print(700 in set2) #är 700 i set2? # nej, det är falskt

for x in set2:
    print(x)

set2.remove(500)
print(set2)
