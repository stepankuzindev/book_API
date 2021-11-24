from marshmallow import Schema, fields

from app.schemas.books import BookResponseSchema


class OrderResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    books = fields.List(fields.Nested(BookResponseSchema))


class OrderListResponseSchema(Schema):
    orders = fields.List(fields.Nested(OrderResponseSchema))
