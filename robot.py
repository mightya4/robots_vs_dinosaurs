from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = None #initialize from weapon class

    def attack(self, dinosaur):
        pass