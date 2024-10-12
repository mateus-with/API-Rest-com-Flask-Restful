from api import mongo

class Player():
    def __init__(self, name, position, age, team, statistics):
        self.name = name
        self.position = position
        self.age = age
        self.team = team
        self.statistics = statistics 
