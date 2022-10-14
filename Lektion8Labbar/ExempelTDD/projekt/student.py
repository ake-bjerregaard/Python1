from projekt import person
class Student(person.Person):
    
    def __init__(self, förnamn, efternamn):
        super().__init__(förnamn, efternamn)
