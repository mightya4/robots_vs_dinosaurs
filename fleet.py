from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots.append(Robot("Xerox the Printer"))
        self.robots.append(Robot("Starbucks the Coffee Dispensor"))
        self.robots.append(Robot("Glitch the Math Matrix"))
    
