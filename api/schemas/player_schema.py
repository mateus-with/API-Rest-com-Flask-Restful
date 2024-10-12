from api import ma
from marshmallow import fields

class PlayerStatisticsSchema(ma.Schema):
    matches_played = fields.Int(required=True)
    goals = fields.Int(required=True)
    assists = fields.Int(required=True)

class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'position', 'age', 'team', 'statistics')

    _id = fields.Str()
    name = fields.Str(required=True)
    position = fields.Str(required=True)
    age = fields.Int(required=True)
    team = fields.Str(required=True)
    statistics = fields.Nested(PlayerStatisticsSchema, required=True)
