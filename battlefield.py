from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.herd.create_herd()
        self.fleet.create_fleet()

        

    def display_welcome(self):
        print("Greetings all we are about to start the Robots vs Dinosaurs battle royal")

    #check which turn + wait some time
    def battle(self):
        pass


    #pass in random turn
    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass
    
    #Create Fleet and create Herd in run game and call the show after every turn
    #show opponents after every turn
    def show_dino_opponent_options(self):
        print("The dinosaur opponent options is as follows: ")
        for robot in self.fleet.robots:
            print(robot.name)

    def show_robo_opponent_options(self):
        print("The robot opponent options is as follows: ")
        for dinosaur in self.herd.dinosaurs:
            print(dinosaur.name)

    def display_winners(self):
        pass