from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = Weapon("Pugil stick", 50)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"You attack for {self.weapon.attack_power}: {dinosaur} health is {dinosaur.health}")