sträng_med_måsvingar_i = "Första argumentet {}  andra argumentet {}  tredje argumentet  {} "


print(sträng_med_måsvingar_i.format("arg1", "arg2", "arg3"))

lista = ["element1", "element2", "element3"]
print(sträng_med_måsvingar_i.format(*lista))  #indikera att man packar upp argument från lista
