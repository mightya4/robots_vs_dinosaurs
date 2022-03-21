from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        num_of_robots = 3
        while len(self.robots) <  num_of_robots:
            robot_name = input("Please enter a name for the robot: ")
            self.robots.append(Robot(robot_name))
    
# f1 = Fleet()
# f1.create_fleet()
# for item in f1.robots:
#     print(item.weapon.name)