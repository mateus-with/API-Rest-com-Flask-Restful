from flask_restful import Resource
from flask import make_response, jsonify, request
from api.schemas.player_schema import PlayerSchema
from ..models.player_model import Player
from ..services.player_service import PlayerService

class PlayerList(Resource):
    def get(self):
        players = PlayerService.get_players()
        player_schema = PlayerSchema(many=True)
        return make_response(player_schema.jsonify(players), 200)

    def post(self):
        player_schema = PlayerSchema()
        validate = player_schema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_player = Player(**json_data)
            result = PlayerService.add_player(new_player)
            res = player_schema.jsonify(result)
            return make_response(res, 201)

class PlayerDetails(Resource):
    def get(self, id):
        player = PlayerService.get_player_by_id(id)
        if player is None:
            return make_response(jsonify("Player not found"), 404)
        player_schema = PlayerSchema()
        return make_response(player_schema.jsonify(player), 200)

    def put(self, id):
        player_bd = PlayerService.get_player_by_id(id)
        if player_bd is None:
            return make_response(jsonify("Player not found"), 404)
        player_schema = PlayerSchema()
        validate = player_schema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            updated_player = Player(**json_data)
            result = PlayerService.update_player(updated_player, id)
            return make_response(player_schema.jsonify(result), 200)

    def delete(self, id):
        player_bd = PlayerService.get_player_by_id(id)
        if player_bd is None:
            return make_response(jsonify("Player not found"), 404)
        PlayerService.delete_player(id)
        return make_response(jsonify("Player deleted successfully"), 200)
