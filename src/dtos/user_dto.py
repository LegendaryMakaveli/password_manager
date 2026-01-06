from marshmallow import Schema, fields, validate

class UserRegisterDTO(Schema):
    email = fields.Email(required=True, validate=validate.Length(min=5, max=100))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=100))

class UserLoginDTO(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class UserResponseDTO(Schema):
    id = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)