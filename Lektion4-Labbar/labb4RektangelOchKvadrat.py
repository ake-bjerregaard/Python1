class Rektangel:

    def __init__(self, bredd_parameter, höjd_parameter): #konstruktorn tar 2 argument, alltså 2 inparametrar
        self.bredd = bredd_parameter
        self.höjd = höjd_parameter

    def area(self):
        return self.bredd * self.höjd

    def omkrets(self):
        return self.bredd * 2 + self.höjd * 2

class Kvadrat:

    def __init__(self, sida):  #konstruktorn tar ett argument
        self.sida = sida

    def area(self):
        return self.sida * self.sida

    def omkrets(self):
        return self.sida * 4


#här nere testar vi koden
enRektangel = Rektangel(10, 25)
enKvadrat = Kvadrat(5)

print("Rektangel")
print(f'Area {enRektangel.area()}') #Area 250
print(f'Omkrets {enRektangel.omkrets()}')#Omkrets 70

print("Kvadrat")
print(f'Area : {enKvadrat.area()}')
print(f'Omkrets : {enKvadrat.omkrets()}')