from api import ma
from marshmallow import fields

class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'position', 'age', 'team')
        
    _id = fields.Str()
    name = fields.Str(required=True)
    position = fields.Str(required=True)
    age = fields.Int(required=True)
    team = fields.Str(required=True)
