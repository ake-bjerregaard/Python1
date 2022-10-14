from projekt.person import Person
class Lärare(Person):
    
    def __init__(self, förnamn, efternamn):
        super().__init__(förnamn, efternamn)