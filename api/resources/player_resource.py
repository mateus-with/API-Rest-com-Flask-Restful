from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import player_schema
from ..models import player_model
from ..services.player_service import PlayerService

class PlayerList(Resource):
    def get(self):
        players = PlayerService.get_players()
        player = player_schema.PlayerSchema(many=True)
        return make_response(player.jsonify(players), 200)
    
    def post(self):
        playerschema = player_schema.PlayerSchema()
        validate = playerschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400) # requisição deu errado
        else:
            json_data = request.get_json()
            new_player = player_model.Player(**json_data)
            result = PlayerService.add_player(new_player)
            res = playerschema.jsonify(result)
            return make_response(res, 201) # Criado
        
class PlayerDetails(Resource):
    def get(self, id):
        player = PlayerService.get_player_by_id(id)
        if player is None:
            return make_response(jsonify("Jogador não encontrado."), 400)
        playerschema = player_schema.PlayerSchema()
        return make_response(playerschema.jsonify(player), 200)
    
    def put(self, id):
        player_bd = PlayerService.get_player_by_id(id)
        if player_bd is None:
            return make_response(jsonify("Jogador não foi encontrado."), 404)
        playerschema = player_schema.PlayerSchema()
        validate = playerschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_player = player_model.Player(**json_data)
            updated_player = PlayerService.update_player(new_player, id)
            return make_response(playerschema.jsonify(updated_player), 200)
        
    def delete(self, id):
        player_bd = PlayerService.get_player_by_id(id)
        if player_bd is None:
            return make_response(jsonify("Jogador não encontrado."), 404)
        PlayerService.delete_player(id)
        return make_response(jsonify("Jogador excluído com sucesso!"), 200)


api.add_resource(PlayerList, '/players')
api.add_resource(PlayerDetails, '/player/<id>')
