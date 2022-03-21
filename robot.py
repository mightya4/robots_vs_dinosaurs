from unicodedata import name


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self. weapon = None #initialize from weapon class