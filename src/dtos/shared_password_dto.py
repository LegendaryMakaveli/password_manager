from marshmallow import Schema, fields, validate

class SharePasswordDTO(Schema):
    password_entry_id = fields.Str(required=True)
    shared_with_email = fields.Email(required=True)
    permission = fields.Str(
        required=True,
        validate=validate.OneOf(["read"])
    )

class SharedPasswordResponseDTO(Schema):
    id = fields.Str(required=True)
    password_entry_id = fields.Str(required=True)
    owner_email = fields.Email(required=True)
    shared_with_email = fields.Email(required=True)
    permission = fields.Str(required=True)
    created_at = fields.DateTime(required=True)