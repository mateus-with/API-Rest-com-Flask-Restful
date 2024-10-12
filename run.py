# Importando o Flask que está em app
from api import app, mongo
from api.models.player_model import Player
from api.services.player_service import PlayerService

if __name__ == '__main__':
    with app.app_context():
        if 'players' not in mongo.db.list_collection_names():
            player = Player(
                name='',
                position='',
                age=0,
                team=''
            )
            PlayerService.add_player(player)
    
    app.run(port=5000, debug=True)
