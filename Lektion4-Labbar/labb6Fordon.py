class Fordon:

    def __init__(self, märke, hastighet, färg, modell, sittplatser, antal_hjul):
        self.märke = märke
        self.hastighet = hastighet
        self.färg = färg
        self.modell = modell
        self.sittplatser = sittplatser
        self.antal_hjul = antal_hjul

    def __str__(self):
        return f"{self.märke} {self.hastighet} {self.färg} {self.modell} {self.sittplatser} {self.antal_hjul}"

class Bil(Fordon):

    def __init__(self, märke, hastighet, färg, modell, sittplatser, bagage_utrymme):
        super().__init__(märke, hastighet, färg, modell, sittplatser, 4)
        self.sidospeglar = 2
        self.bagage_utrymme = bagage_utrymme

    def __str__(self):
        super_strängen = super().__str__()
        return f'{super_strängen} {self.bagage_utrymme}'

class Motorcykel(Fordon):
    
    def __init__(self, märke, hastighet, färg, modell):
        super().__init__(märke, hastighet, färg, modell, 1, 2)
        self.sidospeglar = 2

class VolvoV60(Bil):

    def __init__(self, färg):
        super().__init__("Volvo", 180, färg, "V60", 5, 400)

enMotorCykel = Motorcykel("Honda", 300, "Blå", "Shadow")
enBil = Bil("Volvo", 250, "Svart", "2010", 5, 300)
enVolvoV60 = VolvoV60("gul")


# print(f'{enMotorCykel.märke}, {enMotorCykel.hastighet}, {enMotorCykel.färg}, {enMotorCykel.modell}, {enMotorCykel.antal_hjul}')
print(enMotorCykel)
print(enBil)
print(enVolvoV60)

