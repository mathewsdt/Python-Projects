

# parent class
class Organism:
    name = "unknown"
    species = "unkown"
    legs = None
    arms = None
    dna = "sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrgin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
    

# child class instance
class Human(Organism):
    name = 'Dom'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape"
        return msg

# child class instance

class Dog(Organism):
    name = 'spot'
    species ='canine'
    legs = 4
    arms = 0
    dna = "sequence n"
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg


# child class instance
class Bacterium(Organism):
    name = 'x'
    species = 'bacteria'
    legs = 0
    arms = 0
    dna = 'sequence c'
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two serperate oragnism!"
        return msg
        
    











if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
