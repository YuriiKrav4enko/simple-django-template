from datetime import datetime
from ninja import Schema


class ProductSchema(Schema):
    title: str
    description: str
    created: datetime
    modified: datetime | None = None


ProductListSchema = list[ProductSchema]
