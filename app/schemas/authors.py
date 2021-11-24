from marshmallow import Schema, fields


class AuthorResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class AuthorListResponseSchema(Schema):
    authors = fields.List(fields.Nested(AuthorResponseSchema))
