class Rektangel:

    def __init__(self, bredd_parameter, höjd_parameter): #konstruktorn tar 2 argument, alltså 2 inparametrar
        self.bredd = bredd_parameter
        self.höjd = höjd_parameter

    def area(self):
        return self.bredd * self.höjd

    def omkrets(self):
        return self.bredd * 2 + self.höjd * 2

class Kvadrat(Rektangel):

    def __init__(self, sida):  #konstruktorn tar ett argument
        super().__init__(sida, sida)


#här nere testar vi koden
enRektangel = Rektangel(5, 5)
enKvadrat = Kvadrat(5)

print("Rektangel")
print(f'Area {enRektangel.area()}')
print(f'Omkrets {enRektangel.omkrets()}')

print("Kvadrat")
print(f'Area : {enKvadrat.area()}')
print(f'Omkrets : {enKvadrat.omkrets()}')