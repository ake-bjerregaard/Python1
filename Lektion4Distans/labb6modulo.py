
print(1 % 2)
print(-1 % 2)
print(-1 % 10)

def kolla_om_talet_är_jämnt(tal):
    if tal % 2 == 0:
        print("Talet var jämnt")
    else:
        print("Talet var udda")

kolla_om_talet_är_jämnt(1)
kolla_om_talet_är_jämnt(524)
kolla_om_talet_är_jämnt(1003)

print("------")

def talet_var_delbart_med(nämnare, täljare):
    if nämnare % täljare == 0:
        print(f'Talet {nämnare} var jämnt delbart med {täljare}')
    else:
        print(f'Talet {nämnare} var inte jämnt delbart med {täljare}. Resten var {nämnare%täljare}')

talet_var_delbart_med(5, 10)
talet_var_delbart_med(22, 11)
talet_var_delbart_med(103, 3)

sträng_nämnare = input("Skriv nämnare:")
nämnare = int(sträng_nämnare)
sträng_täljare = input("Skriv täljare:")
täljare = int(sträng_täljare)

talet_var_delbart_med(nämnare, täljare)
