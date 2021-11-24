from marshmallow import Schema, fields

from app.schemas.authors import AuthorResponseSchema


class BookResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    pub_date = fields.Date()
    authors = fields.List(fields.Nested(AuthorResponseSchema))


class BookListResponseSchema(Schema):
    books = fields.List(fields.Nested(BookResponseSchema))
