from datetime import date

class Animal:
    def __init__(self, birthDate):
        self.birthDate = birthDate

    def getAge(self):
        return self.birthDate - date()
    
    def pousseCri(self):
        print('cri')
        
class Chat(Animal):
    def pousseCri(self):
        print('Meow')
        
class Vache(Animal):
    def pousseCri(self):
        print('Mooo')
        
class Poussin(Animal):
    def pousseCri(self):
        print('Piou')

class Ferme:
    nbAnimaux = 0
    
    def __init__(self):
        self.animaux = []

    def ajouteAnimal(self, animal):
        self.animaux.append(animal)
        self.nbAnimaux += 1
        
    def ecouteAnimaux(self):
        for i in range(self.nbAnimaux):
            self.animaux[i].pousseCri()
    
    def main(self):
        self.ajouteAnimal(Chat(date(2020, 1, 2)))
        self.ajouteAnimal(Poussin(date(2024, 1, 2)))
        self.ajouteAnimal(Vache(date(2002, 1, 2)))
        
        self.ecouteAnimaux()

if __name__ == '__main__':
    Ferme().main()