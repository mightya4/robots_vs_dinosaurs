from unicodedata import name
from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(Dinosaur("Keanu the Tyrannosaurus", 20))
        self.dinosaurs.append(Dinosaur("Bertran the Velociraptor", 20))
        self.dinosaurs.append(Dinosaur("Remmy the Pterodactyl", 20))

