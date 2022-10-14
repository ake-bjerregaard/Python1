
class Heltal(int):
    
    def __lt__(self, other): #överskriver less than(__lt__) metoden
        print(f'Det här talet {self} anropade mindre än metoden')
        return super().__lt__(other)
    
variabel1 = Heltal(5)
variabel2 = Heltal(7)
resultat = variabel1 + variabel2

print(f'variabel1: {variabel1}  variabel2: {variabel2}')
print("resultat: ", resultat)

variabelSantEllerFalskt = variabel1 < variabel2
print(variabelSantEllerFalskt)

print("Är variabel1 mindre än variabel2:", variabel1 < variabel2)
print("Är variabel1 mindre än variabel2:", variabel1.__lt__(variabel2))

print("Är variabel1 större än variabel2:", variabel1 > variabel2)
print("Är variabel1 större än variabel2:", variabel1.__gt__(variabel2))