from api import mongo

class Player():
    def __init__(self, name, position, age, team):
        self.name = name
        self.position = position
        self.age = age
        self.team = team
