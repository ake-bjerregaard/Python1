class Person():
    def __init__(self, förnamn, efternamn):
        self.förnamn = förnamn
        self.efternamn = efternamn

    def __str__(self):
        return f'{self.förnamn} {self.efternamn}'