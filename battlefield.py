from dinosaur import Dinosaur
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
        self.battle()

    def is_empty_group(self, some_list):
        if some_list == []:
            return True
        else:
            return False

    def display_welcome(self):
        print("Greetings all we are about to start the Robots vs Dinosaurs battle royal")

    
    def battle(self):
        self.current_turn = None
        while True:
            user_input = int(input("Which opponent will go first? Enter 1 for Dinosaur or Enter 2 for Robot"))
            if user_input == 1:
                
                user_input_one = int(input("Which dinosaur do you want to attack with: "))
                self.current_turn = self.dino_turn(self.herd.dinosaurs[user_input_one])
                self.dino_turn(self.herd.dinosaurs[user_input_one])
                
            elif user_input == 2:
                
                user_input_two = int(input("Which robot do you want to attack with: "))
                self.current_turn = self.robo_turn(self.fleet.robots[user_input_two])
                self.robo_turn(self.fleet.robots[user_input_two])
            else:
                print("Please either 1 or 2.")


            
                


    #pass in random turn
    def dino_turn(self, dinosaur):
        #select one of the dinosaur from the list
        self.show_robo_opponent_options()
        len_of_fleet = len(Fleet().robots)
        fleet_list = Fleet().robots
        user_input = int(input("Which Robot would you like to attack: ")) 
        while user_input > len_of_fleet or user_input < 0:
            user_input = int(input("Which Robot would you like to attack: ")) 
        dinosaur.attack(fleet_list[user_input])
        #check opponent list if empty

    def robo_turn(self, robot):
        self.show_dino_opponent_options()
        len_of_herd = len(Fleet().robots)
        dinosaur_list = Herd().dinosaurs
        user_input = int(input("Which Dinosaur would you like to attack: "))
        while user_input > len_of_herd or user_input < 0:
            user_input = int(input("Which Dinosaur would you like to attack: "))
        robot.attack(dinosaur_list[user_input])
        
        
    
    #Create Fleet and create Herd in run game and call the show after every turn
    #show opponents after every turn
    def show_dino_opponent_options(self):
        print("The dinosaur opponent options is as follows: ")
        for robot in self.fleet.robots:
            self.robot_index = self.fleet.robots.index(robot)
            print(f"{robot.name} : [{self.robot_index}]")

    def show_robo_opponent_options(self):
        print("The robot opponent options is as follows: ")
        for dinosaur in self.herd.dinosaurs:
            self.dino_index = self.herd.dinosaurs.index(dinosaur)
            print(f"{dinosaur.name} : [{self.dino_index}]")

    def display_winners(self):
        pass
        
        
b1 = Battlefield()
b1.run_game()
