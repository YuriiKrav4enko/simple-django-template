from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductModel  # DTO


# Protocol vs ABC ???
class BaseProductService(ABC):  # or IProductService
    # vs code lint don't work
    def get_product_list(
        self, filters: ProductFilters, pagination: PaginationIn,
    ) -> Iterable[Product]:
        raise NotImplementedError

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int:
        ...


# TODO Move filters to service layer to avoid violating D in SOLID
class ORMProductService(BaseProductService):

    def __build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visiable=True)
        if filters.search is not None:
            query &= (Q(title__icontains=filters.search) | Q(description__icontains=filters.search))
        return query

    def get_product_list(self, filters: ProductFilters, pagination: PaginationIn) -> Iterable[Product]:
        query = self.__build_product_query(filters=filters)
        qs = ProductModel.objects.filter(query)[pagination.offset:pagination.offset+pagination.limit]
        return [product.to_entity() for product in qs]

    def get_product_count(self, filters: ProductFilters) -> int:
        query = self.__build_product_query(filters=filters)
        qs = ProductModel.objects.filter(query)
        return qs.count()
