from api import mongo
from ..models import player_model
from bson import ObjectId

class PlayerService:
    def add_player(player):
        result = mongo.db.players.insert_one({
            'name' : player.name,
            'position' : player.position,
            'age' : player.age,
            'team' : player.team,
        })
        return mongo.db.players.find_one({'_id': ObjectId(result.inserted_id)})
    
    @staticmethod
    def get_players():
        return list(mongo.db.players.find())
    
    @staticmethod
    def get_player_by_id(id):
        return mongo.db.players.find_one({'_id' : ObjectId(id)})
    
    def update_player(self, id):
        updated_player = mongo.db.players.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set' : {
                'name' : self.name,
                'position' : self.position,
                'age' : self.age,
                'team' : self.team,
            }},
            return_document=True
        )
        return updated_player
    
    @staticmethod
    def delete_player(id):
        mongo.db.players.delete_one({'_id' : ObjectId(id)})
