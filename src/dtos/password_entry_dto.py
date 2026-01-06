from marshmallow import Schema, fields, validate


class PasswordEntryCreateDTO(Schema):
    title = fields.Str(allow_none=True, validate=validate.Length(max=200))
    url = fields.Str(required=True, validate=validate.Length(min=1, max=500))
    password = fields.Str(required=True, validate=validate.Length(min=1, max=500))
    notes = fields.Str(allow_none=True, validate=validate.Length(max=1000))
    folder_id = fields.Str(allow_none=True)


class PasswordEntryUpdateDTO(Schema):
    title = fields.Str(allow_none=True, validate=validate.Length(max=200))
    url = fields.Str(allow_none=True, validate=validate.Length(min=1, max=500))
    password = fields.Str(allow_none=True, validate=validate.Length(min=1, max=500))
    notes = fields.Str(allow_none=True, validate=validate.Length(max=1000))
    folder_id = fields.Str(allow_none=True)


class PasswordEntryResponseDTO(Schema):
    id = fields.Str(required=True)
    title = fields.Str(allow_none=True)
    url = fields.Str(required=True)
    password = fields.Str(required=True)
    notes = fields.Str(allow_none=True)
    folder_id = fields.Str(allow_none=True)
    user_id = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)


class PasswordEntryListResponseDTO(Schema):
    id = fields.Str(required=True)
    title = fields.Str(allow_none=True)
    url = fields.Str(required=True)
    folder_id = fields.Str(allow_none=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)