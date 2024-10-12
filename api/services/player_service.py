from api import mongo
from bson import ObjectId

class PlayerService:
    # Função para cadastrar um novo jogador
    def add_player(player):
        result = mongo.db.players.insert_one({
            'name': player.name,
            'position': player.position,
            'age': player.age,
            'team': player.team,
            'statistics': player.statistics  # Documento aninhado
        })
        return mongo.db.players.find_one({'_id': ObjectId(result.inserted_id)})
    
    # Função para listar todos os jogadores
    @staticmethod
    def get_players():
        return list(mongo.db.players.find())
    
    # Função para listar um único jogador
    @staticmethod
    def get_player_by_id(id):
        return mongo.db.players.find_one({'_id': ObjectId(id)})
    
    # Função para atualizar um jogador
    @staticmethod
    def update_player(player, id):
        updated_player = mongo.db.players.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {
                'name': player.name,
                'position': player.position,
                'age': player.age,
                'team': player.team,
                'statistics': player.statistics
            }},
            return_document=True
        )
        return updated_player

    @staticmethod
    def delete_player(id):
        mongo.db.players.delete_one({'_id': ObjectId(id)})
