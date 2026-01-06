from marshmallow import Schema, fields, validate

class FolderCreateDTO(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))

class FolderUpdateDTO(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))

class FolderResponseDTO(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    user_id = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)