
class KlassNåtFel():
    
    def __init__(self, namn):
        self.attr = 5
        self.name = namn


enInstans = KlassNåtFel("Johan")
print(enInstans.attr)
print(enInstans.name)
print(enInstans.namn)  ##ger attribute error eftersom instansen av klassen inte har någon variabeln "name"
print(enInstans.finnsEj) #ger attribute error eftersom instansen av klassen inte har någon variabeln "finnsEj"