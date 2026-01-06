from marshmallow import Schema, fields


class PasswordHistoryResponseDTO(Schema):
    id = fields.Str(required=True)
    password_entry_id = fields.Str(required=True)
    password = fields.Str(required=True)
    changed_at = fields.DateTime(required=True)