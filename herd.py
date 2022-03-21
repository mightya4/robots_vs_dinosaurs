from unicodedata import name
from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        num_of_dinosaurs = 3
        while len(self.dinosaurs) < num_of_dinosaurs:
            name_of_dinosaur = input("Please enter a name for the dinosaur: ")
            dinosaur_attack_pwr = input("Please enter the attack power of the dinosaur: ")
            self.dinosaurs.append(Dinosaur(name_of_dinosaur, dinosaur_attack_pwr))

d1 = Herd()
d1.create_herd()

for item in d1.dinosaurs:
    print(item.name)