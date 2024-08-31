from django.db import models

from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel,
)

from core.apps.products.entities.products import Product as ProductEntity


class Product(TimeStampedModel, SoftDeletableModel):
    title = models.CharField(
        verbose_name="Title of the product",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Description of the product",
        blank=True,
    )
    is_visiable = models.BooleanField(
        verbose_name="Visiable of the product in catalog",
        default=True,
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.title

    def to_entity(self) -> ProductEntity:
        # Better to have separate converter
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created=self.created,
            modified=self.modified,
        )
