from datetime import datetime
from ninja import Schema

from core.apps.products.entities.products import Product as ProductEntity


class ProductSchema(Schema):
    id: int
    title: str
    description: str
    created: datetime
    modified: datetime | None = None

    @staticmethod
    def from_entity(entity: ProductEntity) -> 'ProductSchema':
        # It is better to create separate mapper
        return ProductSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            created=entity.created,
            modified=entity.modified
        )
