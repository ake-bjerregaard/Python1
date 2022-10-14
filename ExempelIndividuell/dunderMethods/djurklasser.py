#skapa tre klasser
#skapa en Djur klass
#skapa en Apa klass som ärver utav Djur
#skapa en Elefant klass som ärver utav Djur

class Djur:
    pass

class Apa(Djur):
    
    def __str__(self):
        return "Apan hoppar och äter banan"

class Elefant(Djur):

    def __str__(self):
        return "Dricker vatten"